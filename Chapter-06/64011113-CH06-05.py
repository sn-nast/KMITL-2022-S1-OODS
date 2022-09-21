# Asteroid
def asteroid_collision(asteroid:list, index_asteroid=0):
    if len(asteroid)-1 > index_asteroid:
        left_ast = asteroid[index_asteroid]
        right_ast = asteroid[index_asteroid+1]
            
        if right_ast < 0 and left_ast > 0:
            if abs(left_ast) < abs(right_ast):
                asteroid.pop(index_asteroid)
                asteroid_collision(asteroid, 0)
            elif abs(left_ast) > abs(right_ast):
                asteroid.pop(index_asteroid+1)
                asteroid_collision(asteroid, 0)
            elif abs(right_ast) == abs(left_ast):
                asteroid.pop(index_asteroid)
                asteroid.pop(index_asteroid)
                asteroid_collision(asteroid, 0)
                
        asteroid_collision(asteroid, index_asteroid+1)
    return asteroid

x = input("Enter Input : ").split(",")
# x = "2,-2,3,4".split(",")
x = list(map(int,x))
print(asteroid_collision(x))
