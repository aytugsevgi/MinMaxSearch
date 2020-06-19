
# Oyun Yapay Zeka Algoritması - Minimax Search

Tree sınıfı yarattık.Bu sınıftan oluşturulan nesneler child,depth,value,path özelliklerine sahiptir.
Depth in kökteki değeri 3 tür. Azalarak ağacın aşağı kısmına doğru gider.
Value değerine sadece yaprak kısım sahiptir.Diğer düğümlere ‘None’ değeri atanmıştır
Child 5 elemanlı bir dizidir. O an ki düğümün bağlı olduğu düğümleri barındırır. Yaprak düğümler için bu dizi ‘None’ değerlerine sahiptir.
Path her düğüm için string bir değere sahiptir. Kökte ki düğüm ‘A’ değerine sahiptir.Diğer düğümler projede istenildiği gibi ‘A1523’, ‘A35’,  ‘A1’ gibi değerlere sahiptir.

Program çalıştırıldığında önce kök oluşturulur. ( root = Tree(4,None,’A’) ) şeklinde sırasıyla 
depth, value, path değerleri parametre olarak verilir.
Sonrasında ağacın oluşturulması için “ root.setupGame() “ çalıştırılarak gerekli fonksiyon ile oyun ortamı hazırlanır, tüm düğümler oluşturulup yaprak düğümlere random 1-1000 arasında bir değer atanır.Böylelikle istenen ağaç yapısına ulaşmış oluruz.


Minimax fonksiyonumuz ‘isPlayer’ adında 1 adet parametre alır. Öncelikle bulunduğumuz düğümden gidilebilecek tüm düğümleri ‘children’ değişkenine atar.
Sonrasında 2 for döngüsü içerisinde bu child düğümlerden de gidilebilecek tüm düğümleri ‘children’ dizisine ekler. 

templistsay ve templist değişkenleri sayesinde ‘children’ dizisini slice edip gidilebilmesi mümkün yalnızca yaprak düğümleri elde ediyoruz.Diğer düğümleri istemiyoruz.Bu 2 değişken ile bunu sağladık.

Eğer isPlayer=True ise en yüksek değere sahip düğümü bulup bu düğümü döndürüyoruz.
Eğer isPlayer=False ise en düşük değere sahip düğümü bulup bu düğümü döndürüyoruz.

Bu sayede o düğüme ulaşmak için gidilmesi gereken ilk düğüme ‘player’ veya ‘bilgisayar’ hamlesini yaparak ilerliyor. Algoritmamız basit olarak bu şekilde işlemektedir.

Test etmek için en sonda istediğiniz path’i girip bağlı olan yaprak düğümlerin değerlerini görebilirsiniz.Örneğin ‘A123’ girerek ‘A1231’, ‘A1232’, ‘A1233’, ‘A1234’, ‘A1235’ in değerlerine erişip test edebilirsiniz. Programı sonlandırmak için ‘q’ giriniz.
