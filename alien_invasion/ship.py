import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """ Initialize the ship and set it starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start the new ship at the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

        #store the center of the boat as a decimal value
        self.center = float (self.rect.centerx)
    def update(self):
        """Update the ship's position"""
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -=self.ai_settings.ship_speed_factor

    def blitme(self):
        """Draw the ship"""
        self.screen.blit(self.image, self.rect)
