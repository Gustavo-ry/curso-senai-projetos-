import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen configuration
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Lutadores - Duelando com Armas de Fogo")

# Colors
WHITE = (255, 255, 255)
BG_COLOR = (240, 240, 240)
TEXT_COLOR = (107, 114, 128)
HEADLINE_COLOR = (33, 33, 33)
ACCENT_COLOR = (37, 99, 235)
ACCENT_DARK = (21, 39, 103)
SHADOW_COLOR = (230, 230, 230)
HEALTH_GREEN = (22, 163, 74)
HEALTH_RED = (220, 53, 69)
HEALTH_BG = (200, 200, 200)
BUTTON_BG = (37, 99, 235)
BUTTON_HOVER_BG = (21, 39, 103)
BUTTON_TEXT_COLOR = WHITE
COLOR_CARD_BG = (245, 245, 245)

# Fonts
FONT_HEADLINE = pygame.font.SysFont("Segoe UI", 48, bold=True)
FONT_SCORE = pygame.font.SysFont("Segoe UI", 36, bold=True)
FONT_TEXT = pygame.font.SysFont("Segoe UI", 24)

# Game constants
MAX_HEALTH = 100
WIN_VICTORIES = 5
FPS = 60
CLOCK = pygame.time.Clock()

# Player controls
PLAYER_1_KEYS = {"left": pygame.K_a, "right": pygame.K_d, "attack": pygame.K_w, "special": pygame.K_q}
PLAYER_2_KEYS = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "attack": pygame.K_UP, "special": pygame.K_RSHIFT}

PLAYER_WIDTH = 90
PLAYER_HEIGHT = 140
GROUND_Y = SCREEN_HEIGHT - 150

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed = 10
        self.direction = direction  # 1 for right, -1 for left

    def move(self):
        self.x += self.speed * self.direction

    def draw(self, screen):
        pygame.draw.circle(screen, ACCENT_COLOR, (self.x, self.y), self.radius)

class Fighter:
    def __init__(self, x, y, facing_right=True, color=(30, 30, 30)):
        self.x = x
        self.y = y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.color = color
        self.health = MAX_HEALTH
        self.facing_right = facing_right
        self.speed = 7
        self.is_attacking = False
        self.attack_cooldown = 0
        self.attack_damage = 1
        self.victories = 0
        self.bullets = []
        self.hits_received = 0

    def draw(self, screen):
        body_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, body_rect, border_radius=15)

        # Draw bullets
        for bullet in self.bullets:
            bullet.draw(screen)

        # Draw health bar
        health_bar_width = 200
        health_bar_height = 25
        health_x = self.x + self.width // 2 - health_bar_width // 2
        health_y = self.y - 40
        pygame.draw.rect(screen, HEALTH_BG, (health_x, health_y, health_bar_width, health_bar_height), border_radius=12)
        current_health_width = int((self.health / MAX_HEALTH) * health_bar_width)
        health_color = HEALTH_GREEN if self.health > MAX_HEALTH * 0.3 else HEALTH_RED
        pygame.draw.rect(screen, health_color, (health_x, health_y, current_health_width, health_bar_height), border_radius=12)

    def move_left(self):
        self.x = max(0, self.x - self.speed)
        self.facing_right = False

    def move_right(self):
        self.x = min(SCREEN_WIDTH - self.width, self.x + self.speed)
        self.facing_right = True

    def attack(self):
        if self.attack_cooldown == 0:
            self.is_attacking = True
            self.attack_cooldown = 20

    def special_attack(self):
        if self.attack_cooldown == 0:
            direction = 1 if self.facing_right else -1
            bullet = Bullet(self.x + (self.width if self.facing_right else 0), self.y + self.height // 2, direction)
            self.bullets.append(bullet)
            self.attack_cooldown = 30  # Special attack cooldown

    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.is_attacking = False

        # Move bullets
        for bullet in self.bullets:
            bullet.move()

        # Remove bullets that are off-screen
        self.bullets = [bullet for bullet in self.bullets if 0 < bullet.x < SCREEN_WIDTH]

    def get_hit(self, damage):
        self.health = max(0, self.health - damage)
        self.hits_received += 1

class Button:
    def __init__(self, text, x, y, width, height, font, bg_color, hover_color, text_color=BUTTON_TEXT_COLOR):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.hovered = False

    def draw(self, surface):
        color = self.hover_color if self.hovered else self.bg_color
        pygame.draw.rect(surface, color, self.rect, border_radius=12)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hovered

class FightGame:
    def __init__(self):
        self.player1 = Fighter(150, GROUND_Y, True, (30, 144, 255))
        self.player2 = Fighter(SCREEN_WIDTH - 150 - PLAYER_WIDTH, GROUND_Y, False, (220, 20, 60))
        self.game_active = True
        self.winner = None
        btn_w, btn_h = 180, 50
        self.restart_button = Button("Reiniciar Jogo", SCREEN_WIDTH//2 - btn_w//2, SCREEN_HEIGHT//2 + 100, btn_w, btn_h, FONT_TEXT, BUTTON_BG, BUTTON_HOVER_BG)
        self.player1_hit_this_attack = False
        self.player2_hit_this_attack = False
        self.max_hits = 10

    def draw_health_bars(self):
        p1_text = FONT_SCORE.render(f"Jogador 1: {self.player1.victories} vitórias", True, self.player1.color)
        p2_text = FONT_SCORE.render(f"Jogador 2: {self.player2.victories} vitórias", True, self.player2.color)
        SCREEN.blit(p1_text, (20, 20))
        SCREEN.blit(p2_text, (SCREEN_WIDTH - p2_text.get_width() - 20, 20))

    def check_attacks(self):
        for bullet in self.player1.bullets:
            if bullet.x > self.player2.x and bullet.x < self.player2.x + self.player2.width and bullet.y > self.player2.y and bullet.y < self.player2.y + self.player2.height:
                self.player2.get_hit(self.player1.attack_damage)
                self.player1.bullets.remove(bullet)

        for bullet in self.player2.bullets:
            if bullet.x > self.player1.x and bullet.x < self.player1.x + self.player1.width and bullet.y > self.player1.y and bullet.y < self.player1.y + self.player1.height:
                self.player1.get_hit(self.player2.attack_damage)
                self.player2.bullets.remove(bullet)

    def reset_round(self):
        self.player1.health = MAX_HEALTH
        self.player2.health = MAX_HEALTH
        self.player1.hits_received = 0
        self.player2.hits_received = 0
        self.player1.x = 150
        self.player1.facing_right = True
        self.player2.x = SCREEN_WIDTH - 150 - PLAYER_WIDTH
        self.player2.facing_right = False
        self.player1_hit_this_attack = False
        self.player2_hit_this_attack = False
        self.player1.is_attacking = False
        self.player2.is_attacking = False
        self.player1.attack_cooldown = 0
        self.player2.attack_cooldown = 0

    def update_game_logic(self):
        if not self.game_active:
            return
        self.player1.update()
        self.player2.update()
        self.check_attacks()
        self.player1_hit_this_attack = False
        self.player2_hit_this_attack = False

        if self.player1.hits_received >= self.max_hits:
            self.player2.victories += 1
            self.game_active = False
            self.winner = 2
        elif self.player2.hits_received >= self.max_hits:
            self.player1.victories += 1
            self.game_active = False
            self.winner = 1

        if self.winner:
            if (self.winner == 1 and self.player1.victories >= WIN_VICTORIES) or (self.winner == 2 and self.player2.victories >= WIN_VICTORIES):
                pass
            else:
                self.reset_round()
                self.game_active = True
                self.winner = None

    def draw_interface(self):
        SCREEN.fill(BG_COLOR)
        battle_rect = pygame.Rect(60, 100, SCREEN_WIDTH - 120, SCREEN_HEIGHT - 200)
        shadow_rect = battle_rect.move(10, 10)
        pygame.draw.rect(SCREEN, SHADOW_COLOR, shadow_rect, border_radius=30)
        pygame.draw.rect(SCREEN, COLOR_CARD_BG, battle_rect, border_radius=30)
        headline = FONT_HEADLINE.render("Duelo de Armas de Fogo", True, HEADLINE_COLOR)
        SCREEN.blit(headline, (SCREEN_WIDTH//2 - headline.get_width()//2, 30))
        self.player1.draw(SCREEN)
        self.player2.draw(SCREEN)
        self.draw_health_bars()

        if not self.game_active:
            if self.winner:
                winner_text = f"Jogador {self.winner} venceu esta rodada!"
                if (self.winner == 1 and self.player1.victories >= WIN_VICTORIES) or (self.winner == 2 and self.player2.victories >= WIN_VICTORIES):
                    winner_text = f"Jogador {self.winner} venceu o jogo com {WIN_VICTORIES} vitórias!"
                text_color = HEALTH_GREEN
            else:
                winner_text = "Jogo Pausado"
                text_color = TEXT_COLOR
            winner_surf = FONT_TEXT.render(winner_text, True, text_color)
            SCREEN.blit(winner_surf, (SCREEN_WIDTH//2 - winner_surf.get_width()//2, SCREEN_HEIGHT//2 - 100))
            self.restart_button.update(pygame.mouse.get_pos())
            self.restart_button.draw(SCREEN)

        pygame.display.flip()

    def handle_inputs(self, pressed_keys):
        if not self.game_active:
            return
        if pressed_keys[PLAYER_1_KEYS["left"]]:
            self.player1.move_left()
        if pressed_keys[PLAYER_1_KEYS["right"]]:
            self.player1.move_right()
        if pressed_keys[PLAYER_1_KEYS["attack"]]:
            self.player1.attack()
        if pressed_keys[PLAYER_1_KEYS["special"]]:
            self.player1.special_attack()
        if pressed_keys[PLAYER_2_KEYS["left"]]:
            self.player2.move_left()
        if pressed_keys[PLAYER_2_KEYS["right"]]:
            self.player2.move_right()
        if pressed_keys[PLAYER_2_KEYS["attack"]]:
            self.player2.attack()
        if pressed_keys[PLAYER_2_KEYS["special"]]:
            self.player2.special_attack()

    def restart_game(self):
        self.player1.victories = 0
        self.player2.victories = 0
        self.reset_round()
        self.game_active = True
        self.winner = None

def main():
    game = FightGame()
    running = True
    while running:
        CLOCK.tick(FPS)
        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game.game_active and game.restart_button.is_clicked(event):
                    game.restart_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        game.handle_inputs(pressed_keys)
        game.update_game_logic()
        game.draw_interface()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
