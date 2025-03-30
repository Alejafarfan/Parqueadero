import tkinter as Registro
from datetime import datetime

class RegistroVehiculos:
    def __init__(self):
        self.ventana = Registro.Tk()
        self.ventana.title("Registro de Vehículos")

        # Lista de vehículos registrados
        self.vehiculos = []

        # Labels y Entrys
        self.label_placa = Registro.Label(self.ventana, text="Placa (ABC-123):")
        self.entry_placa = Registro.Entry(self.ventana)

        self.label_marca = Registro.Label(self.ventana, text="Marca:")
        self.entry_marca = Registro.Entry(self.ventana)

        self.label_color = Registro.Label(self.ventana, text="Color:")
        self.entry_color = Registro.Entry(self.ventana)

        self.label_tipo = Registro.Label(self.ventana, text="Tipo (Residente/Visitante):")
        self.entry_tipo = Registro.Entry(self.ventana)

        # Botones
        self.boton_guardar = Registro.Button(self.ventana, text="Guardar", command=self.guardar_vehiculo)
        self.boton_limpiar = Registro.Button(self.ventana, text="Limpiar Campos", command=lambda: self.limpiar_campos())
        self.boton_mostrar = Registro.Button(self.ventana, text="Mostrar Registros", command=self.mostrar_registros)

        # Mensaje de validación y visualización
        self.label_mensaje = Registro.Label(self.ventana, text="", fg="red")
        self.label_registros = Registro.Label(self.ventana, text="", fg="blue", justify="left")

        # Posicionamiento con grid
        self.label_placa.grid(row=0, column=0, padx=5, pady=5)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        self.label_marca.grid(row=1, column=0, padx=5, pady=5)
        self.entry_marca.grid(row=1, column=1, padx=5, pady=5)

        self.label_color.grid(row=2, column=0, padx=5, pady=5)
        self.entry_color.grid(row=2, column=1, padx=5, pady=5)

        self.label_tipo.grid(row=3, column=0, padx=5, pady=5)
        self.entry_tipo.grid(row=3, column=1, padx=5, pady=5)

        self.boton_guardar.grid(row=4, column=0, padx=5, pady=5)
        self.boton_limpiar.grid(row=4, column=1, padx=5, pady=5)
        self.boton_mostrar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.label_mensaje.grid(row=6, column=0, columnspan=2, pady=5)
        self.label_registros.grid(row=7, column=0, columnspan=2, pady=5)

        self.ventana.mainloop()

    def guardar_vehiculo(self):
        """Guarda los datos de un vehículo si los campos no están vacíos."""
        placa = self.entry_placa.get().strip()
        marca = self.entry_marca.get().strip()
        color = self.entry_color.get().strip()
        tipo = self.entry_tipo.get().strip()
        hora_ingreso = datetime.now().strftime("%H:%M:%S")

        if not placa or not marca or not color or not tipo:
            self.label_mensaje.config(text="Todos los campos son obligatorios", fg="red")
            return

        vehiculo = {
            "Placa": placa,
            "Marca": marca,
            "Color": color,
            "Tipo": tipo,
            "Hora Ingreso": hora_ingreso
        }

        self.vehiculos.append(vehiculo)
        self.label_mensaje.config(text="Vehículo registrado exitosamente", fg="green")
        self.limpiar_campos()
    
    def limpiar_campos(self):
        """Limpia todos los campos de entrada."""
        self.entry_placa.delete(0, Registro.END)
        self.entry_marca.delete(0, Registro.END)
        self.entry_color.delete(0, Registro.END)
        self.entry_tipo.delete(0, Registro.END)
        self.label_mensaje.config(text="")

    def mostrar_registros(self):
        """Muestra los registros de vehículos en la consola y en la interfaz."""
        if not self.vehiculos:
            self.label_registros.config(text="No hay registros disponibles", fg="blue")
            return
        registros_texto = ""
        for v in self.vehiculos:
            registros_texto += f"{v['Placa']} - {v['Marca']} - {v['Color']} - {v['Tipo']} - {v['Hora Ingreso']}\n"

        self.label_registros.config(text=registros_texto)
        print("\n--- REGISTROS DE VEHÍCULOS ---")
        for vehiculo in self.vehiculos:
            print(vehiculo)


# Crear instancia del formulario
RegistroVehiculos()
