
# Projeto de Simulação — Otimização da Estratégia de Overbooking

## Descrição

Este repositório contém o projeto **Otimização da Estratégia de Overbooking para Maximização de Receita Através de Simulação de Eventos Discretos**, desenvolvido para fins acadêmicos. O projeto utiliza **Python** e **SimPy** para modelar o processo de reserva de assentos de um voo da companhia fictícia **VoaBrasil Linhas Aéreas**, com foco na rota **São Paulo (Congonhas – SBSP) → Brasília (SBBR)**.

O objetivo é criar um modelo computacional que permita avaliar diferentes níveis de overbooking e identificar aquele que **maximiza a receita líquida esperada por voo**, considerando cancelamentos, no-show e custos de denied boarding.

---

## Objetivos

### Objetivo Geral

Desenvolver um modelo de simulação de eventos discretos capaz de analisar e otimizar a política de overbooking da VoaBrasil na rota SBSP–SBBR.

### Objetivos Específicos

* Modelar a chegada de reservas considerando classes tarifárias.
* Incluir probabilidades de cancelamento e no-show.
* Calcular o trade-off entre custos de spoilage e denied boarding.
* Simular diferentes limites de overbooking.
* Recomendar a política mais rentável com base nos resultados.

---

## Escopo do Projeto

### Inclusões

* Simulação completa do ciclo de reservas de um único voo.
* Consideração de classes tarifárias e comportamentos aleatórios.
* Cálculo de receita líquida:
  **Receita + Multas de cancelamento – Custos de denied boarding**
* Análise comparativa entre cenários usando Monte Carlo.

### Exclusões

* Simulação multi-trecho (conexões).
* Eventualidades externas (clima, manutenção etc.).
* Modelagem de pricing dinâmico.

---

## Metodologia

### 1. Definição do Sistema e Coleta de Dados

* Dados públicos e acadêmicos sobre demanda, cancelamentos e no-show.
* Capacidade da aeronave baseada em modelos como A320/B738.

### 2. Modelagem Conceitual

* Diagrama de atividades representando todas as etapas do processo.
* Entidades (passageiros) e recursos (assentos) definidos.

### 3. Implementação

* Desenvolvimento em **Python** usando a biblioteca **SimPy**.
* Organização modular do código.

### 4. Validação

* Verificação da implementação conforme modelo conceitual.
* Comparação com parâmetros reais da literatura.

### 5. Análise

* Execução de múltiplas replicações (Monte Carlo).
* Comparação estatística entre os cenários simulados.

---

## 📦 Estrutura do Repositório

```
/model/            # Código-fonte da simulação (Python + SimPy)
/docs/             # Relatórios, artefatos e documentação geral
/data/             # Dados externos utilizados (se aplicável)
report.pdf         # Relatório técnico final
presentation.pptx  # Apresentação executiva
README.md          # Este arquivo
```

---

## ▶️ Como Executar

### Requisitos

* Python 3.10 ou superior

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

### Executar o Modelo

```bash
python main.py
```

## Resultados Esperados

* Identificação do nível ótimo de overbooking.
* Minimização de assentos vazios (spoilage).
* Controle dos custos de compensação.
* Relatório final com recomendações gerenciais.

---

## Equipe

* Luísa Caetano        
* Maria Luísa Mendonça 
* Poliana Sousa        
* Victor Luís          

---

## Critérios de Sucesso

* Modelo tecnicamente validado.
* Política ótima de overbooking identificada.
* Trade-off financeiro claramente quantificado.
* Documentação completa e robusta entregue.

---

## Licença

Projeto acadêmico — uso permitido para fins educacionais.
