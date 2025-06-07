import numpy as np


def ask() -> dict[str, str]:
    full_asks = [
        {
            "an_ask": "Por que o Java foi ao terapeuta?",
            "funny_response": "Hmm... essa foi tão ruim que até o NullPointerException chorou.",
            "correct_response": "Porque ele tinha muitos problemas de classe.",
            "want_to_continue": "Mais uma pra conta?",
        },
        {
            "an_ask": "Qual é o algoritmo favorito dos stalkers?",
            "funny_response": "Ok, essa foi mais perdida que um ponteiro sem referência.",
            "correct_response": "Depth First Search.",
            "want_to_continue": "Bora pra próxima?",
        },
        {
            "an_ask": "Como um programador confunde Halloween com Natal?",
            "funny_response": "Sua resposta tem menos sentido que código mal indentado.",
            "correct_response": "Porque OCT 31 == DEC 25.",
            "want_to_continue": "Quer sentir vergonha alheia de novo?",
        },
        {
            "an_ask": "Por que os cientistas de dados são péssimos em esconder segredos?",
            "funny_response": "Essa resposta teve menos privacidade que dataset público.",
            "correct_response": "Porque eles sempre expõem os dados!",
            "want_to_continue": "Continua comigo nessa?",
        },
        {
            "an_ask": "O que o Python disse para o código bagunçado?",
            "funny_response": "Rapaz... essa resposta tá pior que identação errada.",
            "correct_response": "Indentifique-se!",
            "want_to_continue": "A próxima tá melhor, quer ouvir?",
        },
        {
            "an_ask": "Por que o SELECT foi ao psicólogo?",
            "funny_response": "Tá traumatizado de tanto fazer join errado? Igual essa resposta aí...",
            "correct_response": "Porque ele tinha problemas para se relacionar (JOIN).",
            "want_to_continue": "Quer outra piada de programador?",
        },
        {
            "an_ask": "Qual é o animal favorito do SQL?",
            "funny_response": "Com essa resposta, até o INNER JOIN ficou OUTER. 😅",
            "correct_response": "O JOINt-venture!",
            "want_to_continue": "Se quiser mais, é só falar!",
        },
    ]

    random_ask = np.random.randint(low=0, high=(len(full_asks) - 1))

    return full_asks[random_ask].values()  # type: ignore
