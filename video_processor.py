import os
import subprocess
import shutil

class ProcesadorDeVideos:
    def __init__(self, carpeta_entrada, carpeta_salida):
        self.carpeta_entrada = carpeta_entrada
        self.carpeta_salida = carpeta_salida

    def procesar_archivos(self):
        if not os.path.exists(self.carpeta_salida):
            os.makedirs(self.carpeta_salida)

        for raiz, dirs, archivos in os.walk(self.carpeta_entrada):
            dest_raiz = raiz.replace(self.carpeta_entrada, self.carpeta_salida)
            if not os.path.exists(dest_raiz):
                os.makedirs(dest_raiz)

            for archivo in archivos:
                src_archivo = os.path.join(raiz, archivo)
                dest_archivo = os.path.join(dest_raiz, archivo)

                if archivo.endswith(".mp4"):
                    self.procesar_video(src_archivo, dest_archivo)
                else:
                    self.procesar_otro_archivo(src_archivo, dest_archivo)

    def procesar_video(self, archivo_entrada, archivo_salida):
        try:
            if os.path.exists(archivo_salida):
                print(f"El archivo {archivo_salida} ya existe, no se copiará ni codificará.")
                return

            if archivo_entrada.endswith("_codificado.mp4"):
                print(f"El archivo {archivo_entrada} ya está codificado, no se procesará.")
                return

            comando = ["ffmpeg", "-i", archivo_entrada, "-threads", "0", "-c:v", "libx264", "-preset", "slower", "-vtag", "avc1", "-pix_fmt", "yuv420p", "-fflags", "+bitexact", "-c:a", "copy", "-f", "mp4", "-y", archivo_salida]
            subprocess.run(comando)
            os.remove(archivo_entrada)
        except Exception as e:
            print(f"Se produjo un error al procesar el archivo {archivo_entrada}: {e}")

    def procesar_otro_archivo(self, src_archivo, dest_archivo):
        try:
            if os.path.exists(dest_archivo):
                print(f"El archivo {dest_archivo} ya existe, no se copiará.")
                return

            shutil.copy2(src_archivo, dest_archivo)
        except Exception as e:
            print(f"Se produjo un error al procesar el archivo {src_archivo}: {e}")
