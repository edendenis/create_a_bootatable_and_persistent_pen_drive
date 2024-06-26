#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `pen drive bootável e persistente` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `pen drive bootável e persistente` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `pen drive bootável e persistente` on `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `pen drive bootável e persistente`
# 
# Um pen drive bootável e persistente é uma unidade USB que foi configurada para inicializar um sistema operacional diretamente a partir dela, permitindo a execução do sistema operacional em qualquer computador compatível com USB. Além disso, a persistência significa que é possível salvar e manter alterações, arquivos e configurações mesmo após o desligamento do sistema. Isso é útil para executar sistemas operacionais portáteis, como distribuições Linux, com a capacidade de armazenar dados e configurações personalizadas entre sessões de inicialização.
# 

# ## 1. Como configurar/instalar/usar o `pen drive bootável e persistente` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `pen drive bootável e persistente` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para criar um sistema `Linux Ubuntu` persistente em uma unidade USB, você pode seguir estas etapas:
# 
# 1. **Baixe a imagem ISO do Ubuntu:** Primeiro, você precisa baixar a imagem `.iso` mais recente do Ubuntu no site oficial: `Ubuntu Download`.
# 
# 2. **Prepare uma unidade USB:** Você precisará de uma unidade USB com capacidade suficiente para armazenar o `Ubuntu` e seus arquivos persistentes. Certifique-se de fazer backup de todos os dados importantes, pois o processo de criação da unidade USB persistente irá formatar a unidade.
# 
# 3. **Crie um `Live USB` com persistência:** Você pode usar ferramentas como o `Rufus` (para `Windows`) ou o `balenaEtcher` (disponível para Windows, macOS e `Linux`) para gravar a imagem `.iso` do `Ubuntu` na unidade USB.
# 
# 4. **Configure a persistência:** Depois de criar o `Live USB`, você precisará configurar a persistência. Para fazer isso, siga estas etapas:
# 
#     4.1 Inicialize a partir do `Live USB`.
# 
#     4.2 Quando a tela de inicialização aparecer, selecione a opção para inicializar o `Ubuntu Live`.
# 
#     4.3 Uma vez iniciado, abra um terminal.
# 
# 5. **Use o utilitário `mkusb`:** O `mkusb` é um utilitário que pode criar um `Live USB` persistente com facilidade. Você pode instalá-lo e usá-lo para configurar a persistência.
# 
#     5.1 **Instale o `mkusb` com o seguinte comando no terminal:**
# 
#     ```
#     sudo add-apt-repository universe
#     sudo add-apt-repository ppa:mkusb/ppa
#     sudo apt-get update
#     sudo apt-get install mkusb
#     ```
# 
# 6. **Após a instalação, execute o comando `mkusb` no terminal:** `sudo mkusb /dev/sdX`
# 
#     Certifique-se de substituir `/dev/sdX` pelo dispositivo correto da sua unidade USB, você pode usar o comando: `lsblk`. você pode executar o comando `mkusb` enquanto estiver executando o `Live USB` do próprio pendrive. Quando você está usando o `Live USB`, você basicamente está executando o sistema operacional diretamente da unidade USB, então você pode usar o terminal para executar comandos como qualquer outro sistema.
# 
#     Durante o processo, você será solicitado a escolher a opção para criar um sistema persistente. Siga as instruções na tela para configurar a persistência.
# 
#     6.1 Para criar um sistema persistente no `Ubuntu` usando o `mkusb`, você pode escolher a opção: `d:  dus , guidus, mkusb-dus    - Classic, easy to use`
#     
#     Esta é uma versão mais recente e fácil de usar do `mkusb`, projetada para simplificar o processo de criação de unidades USB inicializáveis e persistentes.
# 
#     Portanto, você deve selecionar a opção `"d"` e pressionar `Enter` para usar o `"mkusb"`. Este é um método mais intuitivo e atualizado para criar um sistema persistente no Ubuntu.
# 
# 7. **Aguarde a conclusão:** Após a conclusão do processo, você terá um `Live USB` do `Ubuntu` persistente pronto para uso. Você pode reiniciar o computador e inicializar a partir da unidade USB para testar o sistema persistente.
# 
# Essas etapas devem ajudá-lo a criar um `Live USB` persistente do Ubuntu. Certifique-se de seguir as instruções com cuidado e fazer backup de seus dados importantes antes de prosseguir.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `pen drive bootável e persistente` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Linux Live Persistente?.*** Disponível em: <https://chat.openai.com/c/69f063fb-6cb7-4611-9c48-031595d45d4e> (texto adaptado). Acessado em: 21/03/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 21/03/2024 17:10.
# 
