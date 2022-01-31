# ETSE Warbot
twitter/instagram: @warbot_etse

Este proxecto é un bot de twitter que simula batallas entre estudantes da Escola Técnica Superior de Enxeñería da USC. É un xogo de 0 xogadores, xa que se desenvolve automaticamente, e ten unha duración aproximada de 1,5/2 meses. Foi desenvolvido por Daniel Souto e Anxo Trillo. a finais do 2021. O funcionamento é o seguinte:

Cada día publícanse 3 tweets, que poden ser de batalla ou de alianza. Para as batallas, escóllense dúas persoas ao azar, e elíxese aleatoriamente a unha para que sexa a asesina e outra a víctima. Con cada asesinato, un xogador aumenta os seus puntos de forza, aumentando un pouco as probabilidades de gañar o seguinte combate.

Para as alianzas, elíxense a dúas persoas, que a partir dese momento permanecerán "aliadas": se sae unha elexida como asesina ou víctima, as dúas o serán. Aínda que aumentan as probabilidades de saír escollidas, as alianzas teñen vantaxes: Á hora elexir asasinxs, súmanse os puntos de forza de ambos xogadores, o que aumenta as probabilidades de éxito.

Aínda que non é moi probable, no comezo pode cadrar un xogador contra si mesmo. En tal caso, o publicarase un tweet de "autokill" no que morre por unha causa aleatoria. Tamén pode cadrar que un xogador vaia contra a súa aliada, en tal caso producirase unha traición. Estas dúas opcións están prohibidas cara o final do xogo, pois con poucos xogadores aumentan demasiado as probabilidades de que ocorran.

Á hora de elaborar o contido dos tweets, diferéncianse catro partes:
1. O nome do asasino. Ex: "Manuel García"
2. O verbo de asesinato: Ex: "decapitou"
3. O nome da víctima. Ex: "Felipe Pérez"
4. O modificador. Pode ser unha localización, unha causa, unha motivación... Ex: "na biblioteca"

Cada unha destas catro partes elíxese aleatoriamente dunha lista predefinida. Un exemplo de tweet completo sería: "Manuel García decaptou a Felipe Pérez na biblioteca"

Finalmente, cando só quede un xogador ou unha alianza viva, o xogo rematará.
