from spacy_llm.util import assemble
import os
from dotenv import load_dotenv
from bot_functions import BotFunctions, Fore
import custom_pipeline

load_dotenv()

key = os.getenv("API_KEY")


class SpacyLLMBot:
    def __init__(self):
        self.set_key_env_var()
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.cfg")
        self.nlp = assemble(config_path=config_path)
        self.nlp.add_pipe("custom_lemma")
        self.bot_functions = BotFunctions()

    @staticmethod
    def set_key_env_var():
        os.environ["OPENAI_API_KEY"] = key

    def define_actions(self, action_input):
        actions = []
        for action in action_input:
            if action_input[action]:
                actions.append(action)
        return actions
    
    def compute_actions(self, actions, entities, task):
        for action in actions:
            self.bot_functions.functions[action](entities, task)

    def run(self):
        print(Fore.GREEN + "Вітаю у магазині рослин! Щось підказати?" + Fore.RESET)
        while True:
            user_inp = input("Ваш ввід: ")
            doc = self.nlp(user_inp)
            task = doc.cats
            data = doc.ents
            #print(data)
            #print(task)
            actions = self.define_actions(task)
            if actions:
                self.compute_actions(actions, data, task)
            else:
                print(Fore.GREEN + "Не можу зрозуміти прохання." + Fore.RESET)


bot = SpacyLLMBot()
bot.run()