x11,x12=input().split()
if(x11.isdigit() and x12.isdigit()):
              x11,x12=int(x11),int(x12)
              if(x12==1):
                  print("1 2")
              else:
                 print("1 "+str(x11-x12))
