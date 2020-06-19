import random

class Tree:
    def __init__(self,depth,value,path):
        self.child = [None,None,None,None,None]
        self.depth = depth
        self.value = value
        self.path = path
    def setupGame(self):
        for i in range(5): # 5 child ' a sahip olduğu için döngü 5 kere dönüyor.
            if self.depth == 1: # yapraksa random sayı atanır
                self.child[i] = Tree(self.depth-1,random.randint(1,1001),self.path+str(i+1))
            else: # yaprak değilse value yoktur
                self.child[i] = Tree(self.depth-1,None,self.path+str(i+1))
            if self.depth != 0: #yaprak değilse children oluşturur
                self.child[i].setupGame()


    def minimax(self,isPlayer):
        children = self.getAvailableMoves(self) #bulunduğu node'dan mümkün olan diğer hamleleri çağırır
        templistsay = len(children)
        templist = []
        # yapraklara ulaşmak için sırasıyla currentNode'dan aşağı doğru iniyoruz bu döngüde
        for depth in range(self.depth-1):
            templist = []
            for index in range(templistsay):
                templist += self.getAvailableMoves(children[-(index+1)])
                templistsay = 0
            templistsay += len(templist)
            children += templist
        # currentNode'un tüm alt node'larını içeren listeden sadece yaprak node'ları alıyoruz
        # ve children dizisini bu şekilde güncelliyoruz
        if templist != []:
            children = children[-len(templist):]
        childrenvalue = []
        #bu yaprakların value'larını bir dizide topladık
        for child in children:
            childrenvalue.append(child.value)
        # player için bu değerlerden en yükseğine sahip yaprağı fonksiyon döndürür.
        if isPlayer == True:
            maxIndex = childrenvalue.index(max(childrenvalue))
            maxChild = children[maxIndex]
            return maxChild
        # bilgisayar için bu değerlerden en düşüğüne sahip yaprağı fonksiyon döndürür.
        else:
            minIndex = childrenvalue.index(min(childrenvalue))
            minChild = children[minIndex]
            return minChild

    def gidilebilecekYerlerveDegerleri(self,istenenPath):

        istenenNode = self

        for i in range(len(istenenPath)-len(self.path)):
            istenenNode = istenenNode.child[int(istenenPath[len(istenenNode.path)])-1]
        if ( istenenNode.depth != 0): # yaprak düğüm değil ise
            children = istenenNode.getAvailableMoves(istenenNode)
            templistsay = len(children)
            templist = []
            for depth in range(istenenNode.depth - 1):
                templist = []
                for index in range(templistsay):
                    templist += istenenNode.getAvailableMoves(children[-(index + 1)])
                    templistsay = 0
                templistsay += len(templist)
                children += templist

            if templist != []:
                children = children[-len(templist):]
            childrenvalue = []
            print("********** GİDİLEBİLECEK YERLER VE DEĞERLERİ ***********")
            say = 0  # daha düzenli çıktı verebilmek için oluşturuldu
            for child in children:
                say += 1 # her 5 printten sonra satır başı yapılacak
                print(child.path, "->", child.value, end=' | ')
                if say%5==0:
                    print()
                childrenvalue.append(child.value)
            print("***********     **************     **********")
        else:  # yaprak düğüm ise direkt çocuklarına bakmadan kendi değerlerini yazdırır
            print(istenenNode.path, "->", istenenNode.value)


    def getAvailableMoves(self,node):
        children = []
        for child in node.child:
            children.append(child)
        return children


    def bestMove(self, node):
        bestmovePath = node.path[len(self.path)]
        return bestmovePath

root = Tree(4,None,'A')

print("Oyun oluşturuluyor, sayılar rastgele atanıyor..")
root.setupGame()

currentNode = root



print("Şuan", currentNode.path, "node noktasındasın.")
while(True):
    print("----------------------------------")
    print("Player'ın oynaması bekleniyor..")

    # Kullanıcı oynuyorsa minimax parametresi True, bilgisayarsa False.
    maxChild = currentNode.minimax(True)
    # gidilecek yeri parametre olarak veriyoruz.bize sonraki adımın hamlesini veriyor
    playerbestMove = currentNode.bestMove(maxChild)
    currentNode = currentNode.child[int(playerbestMove) - 1]

    print("Player'ın hamlesi:", currentNode.path)
    print("** Player'ın gitmeye çalıştığı en yüksek Değer ve Path:",maxChild.value,maxChild.path)

    print("----------------------------------")
    print("Bilgisayarın oynaması bekleniyor..")

    minChild = currentNode.minimax(False)
    computerbestMove = currentNode.bestMove(minChild) #bilg.'ın en düşük sayıya götürmesi için gideceği node
    currentNode = currentNode.child[int(computerbestMove)-1]

    print("Bilgisayarın hamlesi:", currentNode.path)
    print("** Bilgisayarın götürmeye çalıştığı en düşük Değer ve Path:",minChild.value,minChild.path)
    print("----------------------------------")

    if (len(currentNode.path) == 5):
        print(currentNode.path, "node'una ulaştınız.")
        print("Puanınız =", currentNode.value)

        gir = input("Test etmek için istediğiniz yaprak düğümlerin değerleri görmek ister misin? e/h:")
        while (gir == 'e' or gir == 'E') and True:
            print("Tüm yaprakları görmek için 'A' giriniz.")
            gir2 = input("Bağlı olduğu yaprakları görmek istediğiniz node'un pathini girin: örn(A12,A145,A5431) or quit(q):")
            if gir2 == 'q' or gir2 == 'Q':
                break
            if len(gir2) > 5 or len(gir2) < 1:
                print("Geçersiz path")
                continue
            root.gidilebilecekYerlerveDegerleri(gir2)
        break