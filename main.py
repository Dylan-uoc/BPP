from ast import arg
import sys
from tabla import*
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
import pandas as pd

class MiApp(QtWidgets.QMainWindow):
	"""Clase para crear una tabla de datos a partir de un archivo excel
	-------------
	Métodos:
	-------------
		abrir_archivo():
			Metodo para abrir un archivo excel, y guardar la direccion en una variable
		crear_tabla():
			Metodo para crear la tabla de datos con los datos del archivo excel
		
	Ejemplo de uso:
	-------------
	>>>> Seleccionar abrir archivo
	>>>> Despues seleccionar mostrar datos
	>>>> Abrir el archivo llamado Lista.xlsx y una vez pasado a dataframe mostrarlo en una tabla
	
	-------------
	Errores:
	>>>> Si el archivo no se puede abrir, se muestra un mensaje de error
	>>>> Si el archivo no tiene el formato correcto, se muestra un mensaje de error
	>>>> Si pulsas en el boton de mostrar datos sin haber abierto un archivo, se muestra un mensaje de error
	
	"""
	def __init__(self):
		""" Constructor de la clase para crear la ventana principal 
		"""		
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)		
		self.ui.bt_abrir.clicked.connect(self.abrir_archivo)
		self.ui.pushButton.clicked.connect(self.crear_tabla)

	def abrir_archivo(self):
		""" Metodo para abrir un archivo excel, y guardar la direccion en una variable

		Args:
			self: self
	
		"""		
		file = QFileDialog.getOpenFileName(self,"Abrir Archivo Excel", "","Excel Files (*.xlsx) ;; All Files (*)")
		self.direccion = file[0]

	def crear_tabla(self):
		""" Metodo para crear la tabla de datos con los datos del archivo excel

		Args:
			self: self
		Returns:
			NoneType: No retorna nada
		"""		
     
		try:	
			df = pd.read_excel(self.direccion)
				
			

			columnas = list(df.columns)
			df_fila = df.to_numpy().tolist()
			x = len(columnas)
			y = len(df_fila)
			
		except ValueError:
			QMessageBox.about (self,'Informacion', 'Formato incorrecto')
			return None			

		except FileNotFoundError:
			QMessageBox.about (self,'Informacion', 'El archivo no se puede abrir')
			return None
		"""Control de errores en caso de que el archivo no se pueda abrir
		"""		
		#print(x, y)
		self.ui.tableWidget.setRowCount(y)
		self.ui.tableWidget.setColumnCount(x)
		"""Se crea la tabla con el numero de filas y columnas correspondientes
		"""
		for j in range(x):
			
			cabecera = QtWidgets.QTableWidgetItem(columnas[j])
			self.ui.tableWidget.setHorizontalHeaderItem(j,cabecera )
			for i in range(y):
				dato = str(df_fila[i][j])
				if dato == 'nan':
					dato =''
				self.ui.tableWidget.setItem(i,j, QTableWidgetItem(dato))
		"""Se crean las cabeceras de la tabla y se llenan con los datos del archivo
		"""		
if __name__ == "__main__":
    """Se crea una instancia de la clase MiApp
		"""    
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    """Se muestra la ventana"""    
    sys.exit(app.exec_())