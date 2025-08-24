# Monitor de CPU e RAM com Arduino + Python  

Este projeto conecta um **Arduino** a um computador via **serial** e exibe em um **LCD** o uso de **CPU** e **RAM** em tempo real.  

---

## ⚙️ Como funciona  

-  O **Python** coleta as informações de uso de CPU e memória RAM usando a biblioteca `psutil`.  
-  Esses dados são enviados pela **porta serial** para o Arduino.  
-  O **Arduino** recebe os valores e exibe no **display LCD**.  

Exemplo no LCD:  

CPU: 
35%


RAM:
62%
            

---

## 🔌 Código Arduino  

- Recebe os dados via `Serial`.  
- Atualiza o display LCD com os valores atuais.  

---

## 📋 Dependências  

### Python  
- `psutil`  
- `pyserial`

### Arduino
- `LiquidCrystal Lib`
