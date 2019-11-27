
teta = 10.0*PI/180 #ângulo inicial
R = 200 #comprimento
g = 980.0 #aceleração da gravidade
vt = 0.0 #velocidade inicial

oldt = millis()/1000.0


def setup():
  size(800,800)
  

def draw():
  global oldt, teta, R, vt, g
  t = millis()/1000.00
  dt = t - oldt
  oldt = t
  
  #componente tangencial da aceleração
  at = -g*sin(teta)
  #atualização de posição e velocidade
  teta += vt*dt/R
  vt += at*dt
  x = R*sin(teta)
  y = R*cos(teta)
  
  background(255)
  stroke(0)
  posx = 400+x
  posy = 200+y
  line(400,200,posx, posy)
  fill(0)
  ellipse(posx,posy,20, 20)
  
  

    
  

  
  