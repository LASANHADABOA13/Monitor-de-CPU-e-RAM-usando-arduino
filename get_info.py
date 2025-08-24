import serial
import psutil
import time

#descubra a porta do arduino e coloque aqui
PORTA_SERIAL = '/caminho/para/porta' 
BAUD_RATE = 9600

print("Iniciando comunicação serial...")

try:
    arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
    time.sleep(2)
    print(f"Conectado ao Arduino na porta {PORTA_SERIAL}")

    while True:
        uso_cpu = int(psutil.cpu_percent(interval=1))

        uso_ram = int(psutil.virtual_memory().percent)

        dados_para_envio = f"C{uso_cpu},R{uso_ram}\n"
        
        arduino.write(dados_para_envio.encode('utf-8'))
        
        print(f"Enviando: CPU={uso_cpu}% | RAM={uso_ram}%")
        
except serial.SerialException as e:
    print(f"Erro: Não foi possível abrir a porta serial {PORTA_SERIAL}.")
    print("Verifique se a porta está correta e se não está sendo usada por outro programa (como o Monitor Serial da IDE).")
except Exception as e:
    print(f"Ocorreu um erro: {e}")