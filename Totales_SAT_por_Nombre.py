#PARA ENCONTRAR TOTALES DE FACTURAS FORMATO SAT

import re
import PyPDF2

def buscar_total_por_nombre(archivo_pdf, nombre_buscado):
    total_sumado = 0.0
    with open(archivo_pdf, "rb") as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina_num in range(len(lector.pages)):
            pagina = lector.pages[pagina_num]
            texto = pagina.extract_text()
            
            # Buscar todas las coincidencias de "Total" y el nombre buscado en el texto
            matches_total = re.findall(r'Total:\s*\$([0-9,]+(?:\.[0-9]+)?)', texto)
            matches_nombre = re.findall(nombre_buscado, texto)
            
            # Iterar sobre cada coincidencia del nombre buscado y encontrar el "Total" más cercano
            for nombre_match in matches_nombre:
                closest_total = None
                min_distance = float('inf')
                nombre_index = texto.index(nombre_match)
                
                # Iterar sobre todas las coincidencias de "Total" para encontrar el más cercano al nombre
                for total_match in matches_total:
                    total_index = texto.index(total_match)
                    distance = abs(total_index - nombre_index)
                    if distance < min_distance:
                        min_distance = distance
                        closest_total = total_match
                
                # Si se encuentra un "Total" cercano, sumarlo al total sumado
                if closest_total:
                    # Imprimir el nombre y el valor antes de sumarlo
                    print(f"Nombre: {nombre_match}, Total: ${closest_total}")
                    total_sumado += float(closest_total.replace(",", ""))
    
    return total_sumado

ruta_archivo = input("Ingrese la ruta del archivo PDF: ")
nombre_buscado = input("Ingrese el nombre a buscar: ")
total_sumado = buscar_total_por_nombre(ruta_archivo, nombre_buscado)
print(f"La suma de los totales para '{nombre_buscado}' es: ${total_sumado}")
