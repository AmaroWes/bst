from node import Node

"""
A função insertRecursion foi baseado no estudo apresentado pela plataforma https://www.geeksforgeeks.org/
"""

class Tree:

    def __init__(self):
        self.root = None

    # Metodo True/False para verificarr se a veriavel raiz não é None.
    def isEmpty(self):
        if not self.root:
            return True
        return False

    # Metodo para inserir Nodo na arvore.
    def insert(self, key):
        if self.isEmpty():
            self.root = Node(key)
        else:
            self.insertRecursion(self.root, key)

    def delete(self, key):
        pass

    def search(self, root, key):
        pass

    # Metodo de inserção rercusivo.
    def insertRecursion(self, root, key):
        # parametro: root, é a raiz original ou da sub-arvore.
        # parametro: key, é o valor que vai ser passado para o Node.
        # Condição de parada: se root for igual a None, ele vai retornar o Node com valor de Key.
        if not root:
            return Node(key)

        # Recurção: se o valor de key for menor que o valor de key da raiz
        # chamos a função novamente mas passado o valor do galho da esquerda da raiz.
        if key < root.key:
            root.left = self.insertRecursion(root.left, key)
        
        # Recurção: se o valor de key for maior que o valor de key da raiz
        # chamos a função novamente mas passado o valor do galho da direita da raiz.
        if key > root.key: 
            root.right = self.insertRecursion(root.right, key)

        # Condição de parada: ao final da função é retornando o propriovalor da raiz, para manter a mesma posição.
        return root

    def searchRecursion(self, root, val):
        # Verifica se o valor da chave é igual ao valor passado por parametro
        # sendo ocaso ele retorna que foi localizado.
        if root.key == val:
            return "Localizado!"

        # verificar se o valor de chave é maior que o valor de val
        # sendo o caso, verifica se existe uma ramificação para esquerda
        # sendo o caso, ele chama novamente a função, repassando a ramificação como a nova árvore.
        if root.key > val and root.left:
           return self.searchRecursion(root.left, val)

        # verifica se o valor da chave é menor que o valor de val
        # sendo o caso, verifica se existe uma ramificação para direita
        # sendo o caso, ele chama novamente a função, repassando a ramificação como a nova árvore.
        if root.key < val and root.right:
           return self.searchRecursion(root.right, val)

        # se nada funcionar, ele retorna que não localizou.
        if not root.right or not root.left:
            return "Não localizado"

    def deleteRecursion(self, root, val, father=None):
        if root.key == val:
            # Verifica se tem os dois filhos
            if root.right and root.left:
                if father:
                    if father.right == root.key:
                        aux = self.getMinRightObj(father.right)
                        if aux.key != father.right.key:
                            aux.left = None
                            aux.right = root.left
                            aux.right.right = root.right
                            father.right = aux

                    if father.left == root.key:
                        aux = self.getMinRightObj(father.left)
                        if aux.key != father.left.key:
                            aux.left = None
                            aux.right = root.left
                            aux.right.right = root.right
                            father.left = aux
                else:
                    aux = self.getMinRightObj(root.right)
                    aux.left = root.left
                    aux.right = root.right
                    self.root = aux

            # verifica se tem um filho
            if root.right or root.left:
                if father:
                    if root.right:
                        if father.right.key == root.key:
                            father.right = root.right
                        else:
                            father.left = root.right
                    elif root.left:
                        if father.right.key == root.key:
                            father.right = root.left
                        else:
                            father.left = root.left
                else:
                    if root.right:
                        self.root = root.right
                    else:
                        self.root = root.left

            # Verifica se não tem filhos
            if not root.right and not root.left:
                if father:
                    if father.left.key == root.key:
                        father.left = None

                    elif father.right.key == root.key:
                        father.right = None
                else:
                    self.root = None
        else:
            if root.key < val:
                self.deleteRecursion(root.right, val, root)

            if root.key > val:
                self.deleteRecursion(root.left, val, root)


    def getMinRightObj(self, root):
        if root.left:
            return self.get_Min_right(root.left)

        if root.right:
            self.get_Min_right(root.right)

        return root

    # Metodo para listar os valores da arvore, em ordem.
    def inOrder(self, root):
        # Parametro: root, valor da raiz da arvore para percorrer, sendo o ponto inicial.
        # Condição de parada: verificar se root é diferente de None.
        if root:
            # chama até o final dos valores a esquerda da arvore
            # retorna esse valor no terminal
            # Passa para o lado direto do valor em aberto no momento
            # e vem retornando os valores, nesse cenário ele vem ordenado do maior ao menor.
            self.inOrder(root.left)
            print(root.key, end=" ")
            self.inOrder(root.right)

    # Metodo para listar os valores da arvore, em pré ordem.
    def preOrder(self, root):
        # Condição de parada
        if root:
            # Começa retornando o valor da raiz passado inicialmente
            # Chaman a função, retornando sempre o valor a esquerda da raiz
            # Indo até o final da arvore, e depois indo para direita
            # retornando a ordem raiz / direita / esquerda / raiz ...
            print(root.key, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    # Metodo para listar os valores da arvore, em pos ordem.
    def postOrder(self, root):
        # Condição de parada
        if root:
            # Começa entrando em todos os valores a esquerda da raiz
            # Chegando no último valor, entrando a direita
            # reiniciando o processo até chegar a condição de parada
            # e então retornando o valor na ordem Esquerda / direita / raiz.
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.key, end=" ")

    # Metodo para pegar o menor número de uma arvore
    def get_Min_right(self, root):
        # verificar se existe um valor na esquerda da raiz temporaria.
        # Sendo o caso, esse valor agora é a raiz.
        # Não sendo o caso ele envia para direita do valor da raiz temporaria, até localizar um valor a esquerda.
        if root.left:
            return self.get_Min_right(root.left)

        if root.right:
            self.get_Min_right(root.right)

        return root.key
