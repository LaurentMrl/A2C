# <span style="color:red">Q-Learning Documentation</span>

Cette doc va généraliser le principe du Q-Learning et son algo de renforcement.

<br>

# <span style="color:red">Q-Function</span>

## Formule de Q-Function :

## <span style="color:red">$Q(s_t, a_t)^\pi$</span>

### <span style="color:red">$Q$</span> : Symbole pour indiquer Q-Function

### <span style="color:red">$s$</span> : State ou l'êtat dans lequel on est <span style="color:green">au moment $t$</span>

### <span style="color:red">$a$</span> : Action que l'on veut effectuer <span style="color:green">au moment $t$</span>

### <span style="color:red">$\pi$</span> : "On suit la policy" : L'agent va faire l'action qu'il lui semble la plus optimisé

<br>

### Formule du nombre de récompenses que je peux avoir dans le futur :

### $Q(s_t, a_t)^\pi = E[R_{t+1} + \gamma * R_{t+2} + \gamma^2 * R_{t+3} + \gamma^3 * R_{t+4}...\gamma^x * R_{t+x+1}|s_t, a_t]$
<br>

### <span style="color:red">$E$</span> : Espérence <span style="color:green">au moment $t$</span> 

### <span style="color:red">$|s_t, a_t]$</span> : Sachant que je suis à l'êtat $s$ <span style="color:green">au moment $t$</span> et que je prends l'action $a$ <span style="color:green">au moment $t$</span>

### <span style="color:red">$\pi$</span> : "On suit la policy" : L'agent va faire l'action qu'il lui semble la plus optimisé

### <span style="color:red">$R_{t}$</span> : Récompense obtenue <span style="color:green">au moment $t$</span>

### <span style="color:red">$\gamma$</span> : gamma ou $\gamma$, chiffre influençant l'importance de la récompense en fonction de quand on obtient la récompense (voir partie sur $\gamma$ gamma)</span>
<br>

# <span style="color:red">$\gamma$ gamma</span>

## gamma ou $\gamma$ est l'importance qu'on donne à la récompense en fonction de l'étape à laquelle on va l'obtenir (Plus la récompense est dans longtemps moins elle a d'importance).

## Exemple : 

## $R_{t+1} + \gamma * R_{t+2}+ \gamma^2 * R_{t+3} + \gamma^3 * R_{t+4}...\gamma^x * R_{t+x+1}$

### Si <span style="color:red">$\gamma$ < 0</span>, alors plus la récompense sera dans longtemps, moins elle aura d'importance.

### Si <span style="color:red">$\gamma$ = 1</span>, on considère que toutes les récompenses ont autant d'importances, peu importe de quand on les obtients.

### Si <span style="color:red">$\gamma$ > 0</span>, alors plus la récompense sera dans longtemps, plus elle aura d'importance.
<br>

# <span style="color:red">Equation de Bellman</span>

## L'equation de Bellman est une version récursive de la formule du nombre de récompenses que je peux avoir dans le futur.
<br>

## $Q(s_t, a_t)^\pi = R + \gamma * (max_{a_{t+1}}Q(s_{t+1}, a_{t+1})^\pi)$