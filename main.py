from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class Paddle(Widget):
    score=NumericProperty(0)
    def bounce_ball(self,ball):
        if self.collide_widget(ball) :
            ball.velocity_x *= -1





class PongBall(Widget):
    velocity_x=NumericProperty(0)
    velocity_y=NumericProperty(0)
    velocity=ReferenceListProperty(velocity_x,velocity_y)#to refer both values at a time
    def move(self,other):
        self.pos=Vector(*self.velocity)+self.pos
        if self.x < 0 :
            self.velocity_x *=-1
            other.player2.score +=1

        if self.x > other.width-50:
            self.velocity_x *=-1
            other.player1.score +=1

        if self.y < 0:
            self.velocity_y *= -1
        if self.y > other.height-50:
            self.velocity_y *= -1





class PongGame(Widget):
    ball=ObjectProperty(None)
    player1=ObjectProperty(None)
    player2=ObjectProperty(None)
    def serve_ball(self):
        self.ball.velocity=Vector(7,0).rotate(randint(0,360))



    def update(self,rps):
        self.ball.move(self)
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width / 4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3 / 4:
            self.player2.center_y = touch.y








class PongApp(App):
    def build(self):
        game=PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/100.0)
        return game


PongApp().run()

