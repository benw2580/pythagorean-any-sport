scored = float(input('Points scored: '))
against = float(input('Points against: '))
games = int(input('Games played: '))

pct_trad = (scored**2)/((scored**2)+(against**2))
wins_trad = games*pct_trad
losses_trad = games-wins_trad

pct_new = (scored**1.83)/((scored**1.83)+(against**1.83))
wins_new = games*pct_new
losses_new = games-wins_new

print(f'Traditional pythagorean winning percentage: {pct_trad:.4f}')
print(f'Traditional pythagorean win-loss record: {wins_trad:.1f}-{losses_trad:.1f} or {wins_trad:.0f}-{losses_trad:.0f}')
print(f'Baseball Reference pythagorean winning percentage: {pct_new:.4f}')
print(f'Baseball Reference pythagorean win-loss record: {wins_new:.1f}-{losses_new:.1f} or {wins_new:.0f}-{losses_new:.0f}')