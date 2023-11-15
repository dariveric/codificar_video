from video_processor import ProcesadorDeVideos

if __name__ == "__main__":
    carpeta_entrada = "d:\\ud\\out_dir\\"
    carpeta_salida = "d:\\out_dir\\"
    procesador = ProcesadorDeVideos(carpeta_entrada, carpeta_salida)
    procesador.procesar_archivos()

