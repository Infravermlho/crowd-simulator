import pygame
from gym_crowdsim.envs.crowd_sim.actor import Actor

clock = pygame.time.Clock()

class CrowdSimEnv:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 600, 400
        self.display = self.weight, self.height = 300, 200

        self.actors = []
        self.selected_actor = 0

    def on_execute(self):
        self.on_init()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            clock.tick(60)
        self.on_cleanup

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf = pygame.Surface((300, 200))

        pygame.display.set_caption("Debugging CrowdSim")

        self.actors.append(Actor(x=120, y=120))

        self._running = True

    def on_loop(self):
        for actor in self.actors:
            actor.update(self.actors)

    def on_render(self):
        self._display_surf.fill((105, 155, 125))
        for actor in self.actors:
            actor.draw(self._display_surf)

        displaysurf = pygame.transform.scale(self._display_surf, self.size)
        self._screen.blit(displaysurf, (0, 0))
        pygame.display.update()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.actors[self.selected_actor].goLeft()
            elif event.key == pygame.K_RIGHT:
                self.actors[self.selected_actor].goRight()
            elif event.key == pygame.K_UP:
                self.actors[self.selected_actor].goUp()
            elif event.key == pygame.K_DOWN:
                self.actors[self.selected_actor].goDown()
            elif event.key == pygame.K_x:
                self.actors[self.selected_actor].stopY()
                self.actors[self.selected_actor].stopX()
                self.selected_actor = (self.selected_actor + 1) % len(self.actors)
                print("[on_event] Ator ativo: " + str(self.selected_actor))
            elif event.key == pygame.K_c:
                self.actors.append(Actor(x=120, y=120))

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.actors[self.selected_actor]._changeX < 0:
                self.actors[self.selected_actor].stopX()
            elif event.key == pygame.K_RIGHT and self.actors[self.selected_actor]._changeX > 0:
                self.actors[self.selected_actor].stopX()
            elif event.key == pygame.K_UP and self.actors[self.selected_actor]._changeY < 0:
                self.actors[self.selected_actor].stopY()
            elif event.key == pygame.K_DOWN and self.actors[self.selected_actor]._changeY > 0:
                self.actors[self.selected_actor].stopY()
                
    def on_cleanup(self):
        pass


if __name__ == "__main__":
    theApp = CrowdSimEnv()
    theApp.on_execute()
