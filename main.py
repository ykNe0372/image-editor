from header import *

# PySide6.QtWidgets.MainWindow を継承して class 定義
class MainWindow(QMainWindow):
    def __init__(self):                         # コンストラクタ（初期化）
        super().__init__()                      # 親コンストラクタの呼び出し
        self.setWindowTitle("画像加工アプリ")   # ウィンドウタイトルを設定
        self.setGeometry(100, 30, 1000, 600)    # ウィンドウ位置を設定

        self.current_pixmap = None
        self.image_label = QLabel()
        self.scroll_area = QScrollArea(self)

        self.scroll_area.setWidgetResizable(True)
        self.setCentralWidget(self.scroll_area)

        self.scroll_area.setWidget(self.image_label)
        self.image_label.setAlignment(Qt.AlignVCenter) # 左端中央に表示

        # メニューバー表示
        self.create_menu()

    # ファイルを開く
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "ファイルを開く", "", "Images (*.jpg *.png *.gif)")
        self.show_image(file_name)

    # ファイルを表示
    def show_image(self, file_name):
        self.current_pixmap = QPixmap(file_name)
        # 画像サイズが大きすぎたらある程度小さくする
        self.current_pixmap = self.current_pixmap.scaled(900, 900, PySide6.QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label.setPixmap(self.current_pixmap)

    # 画像を保存
    # ダイアログは出るが、保存する画像が指定できていない？
    def save_image(self):
        file_rename, _ = QFileDialog.getSaveFileName(self, "名前を付けて保存", os.path.expanduser('') + '/untitled', "Images(*.jpg *.png *.gif)")
        if file_rename == "":
            pass

    # 終了
    def exit_application(self):
        self.close()

    # 明るさ・コントラスト
    def BC_edit(self):
        pass

    def BC_change(self):
        pass

    # 色相・彩度・明度
    def HSV_edit(self):
        pass

    # メニューバーの項目と設定
    def create_menu(self):
        menu_bar = self.menuBar()
        
        # ファイル（F）
        file_menu = menu_bar.addMenu("ファイル（&F）")
        
        open_action = QAction("開く（&O）", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("保存（&S）", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_image)
        file_menu.addAction(save_action)
        save_action.setEnabled(False) # 未完成なのでグレードアウト

        exit_action = QAction("終了（&X）", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_application)
        file_menu.addAction(exit_action)

        # 編集（E）
        edit_menu = menu_bar.addMenu("編集（E）")

        BC_action = QAction("明るさ・コントラスト（&C）", self)
        BC_action.triggered.connect(self.BC_edit)
        edit_menu.addAction(BC_action)
        BC_action.setEnabled(False) # 未完成なのでグレードアウト

        HSV_action = QAction("色相・彩度・明度（&H）", self)
        HSV_action.triggered.connect(self.HSV_edit)
        edit_menu.addAction(HSV_action)
        HSV_action.setEnabled(False) # 未完成なのでグレードアウト

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()