
# Hogwarts Legacy Switch Mod Manager
**Important: Mods only work on Nintendo Switch consoles with a modified firmware running Atmosphere.**

**Importante: Os mods só funcionam em consoles Nintendo Switch com o firmware modificado utilizando o Atmosphere.**


🇺🇸 English
This is a simple program designed to organize mods for Hogwarts Legacy on the Nintendo Switch. It allows users to select .pak files and automatically places them in the correct folder structure required by Atmosphere.

Only .pak format mods are compatible with the Nintendo Switch.
Mods that use additional textures or extra files are not supported and will not work.

This project is the beginning of a mod manager for the Switch, and we plan to add support for more games and additional features in the future.

🇧🇷 Português
Este é um programa simples desenvolvido para organizar mods do jogo Hogwarts Legacy no Nintendo Switch. Ele permite ao usuário selecionar arquivos .pak e os coloca automaticamente na estrutura de pastas correta exigida pelo Atmosphere.

Apenas mods no formato .pak são compatíveis com o Nintendo Switch.
Mods que utilizam texturas adicionais ou arquivos extras não são compatíveis e não funcionarão.

Este projeto é o início de um gerenciador de mods para o Switch, e planejamos adicionar suporte a mais jogos e funcionalidades adicionais no futuro.


## Documentação
🇺🇸 English
How to Use
Run the program (mod_manager.exe if compiled, or python mod_manager.py).

Click "Select .pak Files" to choose the mod files you want to install.

Click "Create Folders and Copy Files".

The program will create a folder called mod_manager inside your Documents folder.

Inside mod_manager, the following structure will be generated:

```
mod_manager/
└── hogwarts_legacy/
    └── atmosphere/
        └── Contents/
            └── 0100F7E00C70E000/
                └── Romfs/
                    └── Phoenix/
                        └── Content/
                            └── Paks/
                                └── ~mods/
                                    └── your_mods.pak
```
Open the folder using the "Open Destination Folder" button.

Copy everything from inside the hogwarts_legacy folder to the root of your SD card, where Atmosphere is installed.

Command Line Usage
You can also run the program from the command line and provide .pak files directly:

```
python mod_manager.py mod1.pak mod2.pak
```
These files will be automatically added to the list and copied when you click the "Create Folders and Copy Files" button.

Important Notes
Only .pak mods are compatible with the Nintendo Switch.

Mods that use additional textures or extra files will not work on Switch.

More games and new features will be supported in the future.

🇧🇷 Português
Como Usar
Execute o programa (mod_manager.exe se estiver compilado ou python mod_manager.py).

Clique em "Selecionar Arquivos .pak" para escolher os mods que deseja instalar.

Clique em "Criar Pastas e Copiar Arquivos".

O programa vai criar uma pasta chamada mod_manager dentro da sua pasta Documentos.

Dentro da pasta mod_manager, será gerada a seguinte estrutura:

```
mod_manager/
└── hogwarts_legacy/
    └── atmosphere/
        └── Contents/
            └── 0100F7E00C70E000/
                └── Romfs/
                    └── Phoenix/
                        └── Content/
                            └── Paks/
                                └── ~mods/
                                    └── seus_mods.pak
```
Abra a pasta pelo botão "Abrir Pasta de Destino".

Copie tudo que está dentro da pasta hogwarts_legacy para a raiz do seu cartão SD, onde o Atmosphere está instalado.

Uso por Linha de Comando
Você também pode rodar o programa via terminal e informar os arquivos .pak diretamente:
```
python mod_manager.py mod1.pak mod2.pak
```
Esses arquivos serão adicionados automaticamente à lista e copiados quando você clicar em "Criar Pastas e Copiar Arquivos".

Notas Importantes
Apenas mods .pak são compatíveis com o Nintendo Switch.

Mods que utilizam texturas adicionais ou arquivos extras não são compatíveis e não funcionarão.

Mais jogos e funcionalidades serão adicionados no futuro.

