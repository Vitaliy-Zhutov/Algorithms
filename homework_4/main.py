from red_black_tree import RedBlackTree

if __name__ == '__main__':
    tree = RedBlackTree()
    print('\'q\' - выход. Добавляйте числовые значения для размещения узлов дерева:')
    while True:
        tree.print_tree()
        try:
            user_input = input('> ')
            if user_input == 'q':
                print('---- Программа завершена ----')
                break
            node = tree.add_node(int(user_input))
        except ValueError:
            print('> Некорректный ввод ')
            