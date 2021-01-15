def countdown(x,y):
       if x==0 or y==0:
              print("boom")
       else:
              print("x",x)
              print("y",y)
              countdown(x-1,y)
              countdown(x,y-2)
countdown(20,20)