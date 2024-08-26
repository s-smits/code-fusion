# CodeFusion: LLM code kiezer

CodeFusion is een handige Python-tool waarmee je de output van verschillende AI-modellen kunt vergelijken voor je coding vragen. De app ondersteunt modellen van grote spelers zoals Google, Anthropic, OpenAI en Meta, en zet hun antwoorden netjes naast elkaar.

## Setup

1. Clone de repo en ga naar de projectfolder:
   ```
   git clone https://github.com/s-smits/code-fusion
   cd code-fusion
   ```

2. Maak een virtual environment en activeer 'm:
   - Mac en Linux:
     ```
     python3 -m venv venv_codefusion
     source venv_codefusion/bin/activate
     ```
   - Windows:
     ```
     python -m venv venv_codefusion
     venv_codefusion\Scripts\activate
     ```

3. Installeer de benodigde packages:
   ```
   pip install -r requirements.txt
   ```

4. Maak een `.env` file in de root van je project en zet je API keys erin:
   ```
   GOOGLE_API_KEY=jouw_google_api_key
   ANTHROPIC_API_KEY=jouw_anthropic_api_key
   OPENAI_API_KEY=jouw_openai_api_key
   OPENROUTER_API_KEY=jouw_openrouter_api_key
   ```

   Je hoeft alleen de keys toe te voegen voor de modellen die je wilt gebruiken.

## Aan de slag

Run het script:
```
python codefusion.py
```

De app doet het volgende:
1. Vraagt je om minstens twee AI-modellen te kiezen
2. Checkt of je API keys hebt ingevuld (of vraagt erom als ze ontbreken)
3. Laat je programmeervragen stellen
4. Toont live de antwoorden van de gekozen modellen
5. Geeft een samenvatting van de verschillen tussen de antwoorden
6. Adviseert kort welk model het beste lijkt voor jouw vraag

Type 'quit' om de app af te sluiten.

## Features

- Parallel querien van meerdere AI-modellen
- Live weergave van de antwoorden
- Automatische retry bij API-fouten
- Summary en advies via GPT-4o-mini
- Fancy console-interface met gekleurde output

## Requirements

Check `requirements.txt` voor de complete lijst. De belangrijkste libraries zijn:
- litellm
- rich
- python-dotenv

## License

[MIT License](LICENSE)

## Demo
[<video src="https://github.com/user-attachments/assets/-" controls="controls" style="max-width: 730px;">
</video>](https://github.com/user-attachments/assets/9aa20948-4ddf-4447-b8ab-607ad2ea10da
)
