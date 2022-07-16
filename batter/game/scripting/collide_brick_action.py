from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        balls = cast.get_actors(BALL_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP) 
        
        balls_to_remove = set()
        bricks_to_remove = set()
        
        for ball in balls:
            for brick in bricks:
                ball_body = ball.get_body()
                brick_body = brick.get_body()

                if self._physics_service.has_collided(ball_body, brick_body):
                
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    points = brick.get_points()
                    stats.add_points(points)
                    balls_to_remove.add(ball)
                    bricks_to_remove.add(brick)
             
            # if len(balls_to_remove) > 0:       
            #     print(len(balls_to_remove))
            #     print(len(bricks_to_remove))
        for brick in bricks_to_remove:
            
            cast.remove_actor(BRICK_GROUP, brick)
       
        for ball in balls_to_remove:
            cast.remove_actor(BRICK_GROUP, ball)
              
           
           