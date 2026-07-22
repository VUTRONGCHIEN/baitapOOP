def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams_2():
    do_twice(print_beam)
    print('+')

def print_posts_2():
    do_twice(print_post)
    print('|')

def print_row_2():
    print_beams_2()
    do_four(print_posts_2)

def draw_grid_2x2():
    do_twice(print_row_2)
    print_beams_2()

print("--- LƯỚI 2x2 ---")
draw_grid_2x2()

def print_beams_4():
    do_four(print_beam)
    print('+')

def print_posts_4():
    do_four(print_post)
    print('|')

def print_row_4():
    print_beams_4()
    do_four(print_posts_4)

def draw_grid_4x4():
    do_four(print_row_4)
    print_beams_4()

print("\n--- LƯỚI 4x4 ---")
draw_grid_4x4()