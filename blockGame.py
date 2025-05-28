import pygame
import random

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# Game settings
BLOCK_SIZE = 30   # Size of each block in pixels
GRID_WIDTH = 10   # Width of the game grid (10 blocks)
GRID_HEIGHT = 20  # Height of the game grid (20 blocks)
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
GAME_AREA_LEFT = BLOCK_SIZE

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I-Piece
    [[1, 1], [1, 1]],  # O-piece
    [[1, 1, 1], [0, 1, 0]],  # T-piece
    [[1, 1, 1], [1, 0, 0]],  # J-piece
    [[1, 1, 1], [0, 0, 1]],  # L-piece
    [[0, 1, 1], [1, 1, 0]],  # S-piece
    [[1, 1, 0], [0, 1, 1]]   # Z-piece
]

SHAPE_COLORS = [CYAN, YELLOW, PURPLE, BLUE, ORANGE, GREEN, RED]

class Tetrimino:
    def __init__(self):
        # Starting point 
        self.shape_idx = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[self.shape_idx]
        self.color = SHAPE_COLORS[self.shape_idx]
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0
        
    def rotate(self):
        # Transpose the shape matrix and reverse each row to rotate 90 degrees
        rows = len(self.shape)
        cols = len(self.shape[0])
        rotated = [[0 for _ in range(rows)] for _ in range(cols)]
        
        for r in range(rows):
            for c in range(cols):
                rotated[c][rows - 1 - r] = self.shape[r][c]
                
        return rotated

class BlockGame:
    def __init__(self):

        #Game Window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Block Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Italic', 25)
        self.reset_game()
        
    def reset_game(self):
        #reset block
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetrimino()
        self.next_piece = Tetrimino()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_speed = 0.5  # seconds
        self.fall_time = 0
        
    def draw_grid(self):
        # Draw the game area border
        pygame.draw.rect(self.screen, WHITE, 
                         (GAME_AREA_LEFT - 2, 0, 
                          GRID_WIDTH * BLOCK_SIZE + 4, 
                          GRID_HEIGHT * BLOCK_SIZE + 4), 2)
        
        # Draw the grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(self.screen, GRAY, 
                                 (GAME_AREA_LEFT + x * BLOCK_SIZE, 
                                  y * BLOCK_SIZE, 
                                  BLOCK_SIZE, BLOCK_SIZE), 1)
                
        # Draw the placed pieces
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, SHAPE_COLORS[self.grid[y][x] - 1],
                                    (GAME_AREA_LEFT + x * BLOCK_SIZE + 1,
                                     y * BLOCK_SIZE + 1,
                                     BLOCK_SIZE - 2, BLOCK_SIZE - 2))
                    
    def draw_current_piece(self):
         # Draws the currently falling piece
        for y in range(len(self.current_piece.shape)):
            for x in range(len(self.current_piece.shape[0])):
                if self.current_piece.shape[y][x]:
                    pygame.draw.rect(self.screen, self.current_piece.color,
                                    (GAME_AREA_LEFT + (self.current_piece.x + x) * BLOCK_SIZE + 1,
                                     (self.current_piece.y + y) * BLOCK_SIZE + 1,
                                     BLOCK_SIZE - 2, BLOCK_SIZE - 2))
    
    def draw_next_piece(self):
        next_text = self.font.render("Next:", True, WHITE)
        self.screen.blit(next_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 20, 30))
        
        next_x = GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 50
        next_y = 80
        
        for y in range(len(self.next_piece.shape)):
            for x in range(len(self.next_piece.shape[0])):
                if self.next_piece.shape[y][x]:
                    pygame.draw.rect(self.screen, self.next_piece.color,
                                    (next_x + x * BLOCK_SIZE + 1,
                                     next_y + y * BLOCK_SIZE + 1,
                                     BLOCK_SIZE - 2, BLOCK_SIZE - 2))
    
    def draw_score(self):
        # Draws score, level, and lines cleared
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        lines_text = self.font.render(f"Lines: {self.lines_cleared}", True, WHITE)
        
        self.screen.blit(score_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 20, 180))
        self.screen.blit(level_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 20, 220))
        self.screen.blit(lines_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 20, 260))
    
    def draw_game_over(self):
        # Shows "GAME OVER" message when appropriate
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, RED)
            restart_text = self.font.render("Press R to restart", True, WHITE)
            
            self.screen.blit(game_over_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE // 2 - 80, 
                                            GRID_HEIGHT * BLOCK_SIZE // 2 - 30))
            self.screen.blit(restart_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE // 2 - 100, 
                                          GRID_HEIGHT * BLOCK_SIZE // 2 + 10))
    
    def valid_position(self, shape=None, x=None, y=None):
         # Checks if a piece can be placed at given position
        # Prevents out-of-bounds and collisions
        if shape is None:
            shape = self.current_piece.shape
        if x is None:
            x = self.current_piece.x
        if y is None:
            y = self.current_piece.y
            
        for py in range(len(shape)):
            for px in range(len(shape[0])):
                if shape[py][px]:
                    # Check if out of bounds
                    if (x + px < 0 or x + px >= GRID_WIDTH or 
                        y + py >= GRID_HEIGHT):
                        return False
                    # Check if collides with placed pieces
                    if y + py >= 0 and self.grid[y + py][x + px]:
                        return False
        return True
    
    def merge_piece(self):
        # Adds the current piece to the grid when it lands
        for y in range(len(self.current_piece.shape)):
            for x in range(len(self.current_piece.shape[0])):
                if self.current_piece.shape[y][x]:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.shape_idx + 1
    
    def clear_lines(self):
         # Checks for completed lines, removes them, and updates score
        # Scoring: 100 for 1 line, 300 for 2, 500 for 3, 800 for 4 (Tetris)
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_to_clear.append(y)
        
        for line in lines_to_clear:
            del self.grid[line]
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
            
        # Update score
        if len(lines_to_clear) > 0:
            self.lines_cleared += len(lines_to_clear)
            self.score += [100, 300, 500, 800][min(len(lines_to_clear) - 1, 3)] * self.level
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(0.05, 0.5 - (self.level - 1) * 0.05)
    
    def new_piece(self):
        # Spawns a new piece and checks for game over
        self.current_piece = self.next_piece
        self.next_piece = Tetrimino()
        
        # Check if game over
        if not self.valid_position():
            self.game_over = True
    
    def handle_input(self):
        # Processes keyboard input:
        # - Arrow keys for movement
        # - Up for rotation
        # - Space for hard drop
        # - R to restart
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset_game()
                else:
                    if event.key == pygame.K_LEFT:
                        if self.valid_position(x=self.current_piece.x - 1):
                            self.current_piece.x -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.valid_position(x=self.current_piece.x + 1):
                            self.current_piece.x += 1
                    elif event.key == pygame.K_DOWN:
                        if self.valid_position(y=self.current_piece.y + 1):
                            self.current_piece.y += 1
                    elif event.key == pygame.K_UP:
                        rotated = self.current_piece.rotate()
                        if self.valid_position(shape=rotated):
                            self.current_piece.shape = rotated
                    elif event.key == pygame.K_SPACE:
                        # Hard drop
                        while self.valid_position(y=self.current_piece.y + 1):
                            self.current_piece.y += 1
                        self.merge_piece()
                        self.clear_lines()
                        self.new_piece()
        
        return True
    
    def update(self, delta_time):
        if self.game_over:
            return
            
        self.fall_time += delta_time
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0
            if self.valid_position(y=self.current_piece.y + 1):
                self.current_piece.y += 1
            else:
                self.merge_piece()
                self.clear_lines()
                self.new_piece()
    
    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        self.draw_current_piece()
        self.draw_next_piece()
        self.draw_score()
        self.draw_game_over()
        pygame.display.flip()
    
    def run(self):
        #game loop 
        running = True
        last_time = pygame.time.get_ticks()
        
        while running:
            # Calculate time since last frame
            current_time = pygame.time.get_ticks()
            delta_time = (current_time - last_time) / 1000.0  # Convert to seconds
            last_time = current_time
            
            # Handle input, update game state, draw frame
            running = self.handle_input()
            self.update(delta_time)
            self.draw()
            
            # Cap at 60 FPS
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    game = BlockGame()
    game.run()