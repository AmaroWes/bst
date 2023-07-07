from tree import Tree

tr = Tree()
tr2 = Tree()

# Testando os inserts
print("Testando os inserts\n")
tr.insert(8)
tr.insert(3)
tr.insert(1)
tr.insert(6)
tr.insert(4)
tr.insert(7)
tr.insert(10)
tr.insert(14)
tr.insert(13)
"""
print("Testeando os retornos\n")
tr.inOrder(tr.root)
print("")
tr.preOrder(tr.root)
print("")
tr.postOrder(tr.root)"""

print("\nTestando o menor valor\n")
print(tr.get_Min_right(tr.root.right))

"""print("Testando o search")
print(tr.searchRecursion(tr.root, 13))
print(tr.searchRecursion(tr.root, 0))
print(tr.searchRecursion(tr.root, 500))"""

print("Testando os delete")
tr.deleteRecursion(tr.root, 1)
tr.deleteRecursion(tr.root, 6)
tr.inOrder(tr.root)
print("\n")

"""
# Segundo teste
tr2.insert(100)
tr2.insert(20)
tr2.insert(200)
tr2.insert(10)
tr2.insert(30)
tr2.insert(150)
tr2.insert(300)

tr2.inOrder(tr2.root)
print(" ")
tr2.preOrder(tr2.root)
print(" ")
tr2.postOrder(tr2.root)

print(tr2.get_Min_right(tr2.root.right))
print(tr2.search(tr2.root, 150))
print(tr2.search(tr2.root, 0))
print(tr2.search(tr2.root, 500))
"""