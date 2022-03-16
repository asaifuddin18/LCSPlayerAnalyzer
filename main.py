import matplotlib.pyplot as plt
import csv
from objects.player import Player
import matplotlib.patches as patches
import pandas as pd
import numpy as np
players = []
df = None
with open("data/totals.csv") as f:
    csv_file = csv.reader(f, delimiter=',')
    for row in csv_file:
        temp = Player(row)
        players.append(temp)
    df = pd.read_csv("data/totals.csv")

df_jng = df[df['role'] == 'jng']
df_jng = df_jng.sort_values('player_kills')

#junglers = [x for x in players if x.role == 'jng']
#junglers.sort(key=lambda x: x.player_kills)

fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
ax.vlines(x=np.arange(10), ymin=0, ymax=df_jng.player_kills, color='firebrick', alpha=0.7, linewidth=20)

ax.set_title('LCS Jungler Player Kills', fontdict={'size':22})
ax.set(ylabel='Total kills', ylim=(0, max(df_jng['player_kills'])))
plt.xticks(np.arange(10), df_jng.player, rotation=60, horizontalalignment='right', fontsize=12)

p1 = patches.Rectangle((.51, -.02), width=.39, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
p2 = patches.Rectangle((.124, -.02), width=.386, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)
plt.savefig('./figs/jg_kill_rank.png')
#plt.show()


df_jng = df_jng.sort_values('player_deaths', ascending=False)
fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
ax.vlines(x=np.arange(10), ymin=0, ymax=df_jng.player_deaths, color='firebrick', alpha=0.7, linewidth=20)
ax.set_title('LCS Jungler Player Deaths', fontdict={'size':22})
ax.set(ylabel='Total Deaths', ylim=(0, max(df_jng['player_deaths'])))
plt.xticks(np.arange(10), df_jng.player, rotation=60, horizontalalignment='right', fontsize=12)
p1 = patches.Rectangle((.51, -.02), width=.39, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
p2 = patches.Rectangle((.124, -.02), width=.386, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)
plt.savefig('./figs/death_rank.png')
#plt.show()

df_jng['player_kd'] = df_jng['player_kills'] / df_jng['player_deaths']
df_jng = df_jng.sort_values('player_kd')
fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
ax.vlines(x=np.arange(10), ymin=0, ymax=df_jng.player_kd, color='firebrick', alpha=0.7, linewidth=20)
ax.set_title('LCS Jungler Player K/D', fontdict={'size':22})
ax.set(ylabel='K/D', ylim=(0, max(df_jng['player_kd'])))
plt.xticks(np.arange(10), df_jng.player, rotation=60, horizontalalignment='right', fontsize=12)
p1 = patches.Rectangle((.51, -.02), width=.39, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
p2 = patches.Rectangle((.124, -.02), width=.386, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)
plt.savefig('./figs/k_d.png')
#plt.show()

df_jng = df_jng.sort_values('player_kda')
fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
ax.vlines(x=np.arange(10), ymin=0, ymax=df_jng.player_kda, color='firebrick', alpha=0.7, linewidth=20)
ax.set_title('LCS Jungler Player K/D/A', fontdict={'size':22})
ax.set(ylabel='K/D/A', ylim=(0, max(df_jng['player_kda'])))
plt.xticks(np.arange(10), df_jng.player, rotation=60, horizontalalignment='right', fontsize=12)
p1 = patches.Rectangle((.51, -.02), width=.39, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
p2 = patches.Rectangle((.124, -.02), width=.386, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)
plt.savefig('./figs/k_d_a.png')
#plt.show()

df_jng['damage_efficiency'] = df_jng['total_player_dmg_to_champs'] / df_jng['total_player_gold']
df_jng = df_jng.sort_values('damage_efficiency')
fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
ax.vlines(x=np.arange(10), ymin=0, ymax=df_jng.damage_efficiency, color='firebrick', alpha=0.7, linewidth=20)
ax.set_title('LCS Jungler Player Damage Efficiency', fontdict={'size':22})
ax.set(ylabel='K/D', ylim=(0, max(df_jng['damage_efficiency'])))
plt.xticks(np.arange(10), df_jng.player, rotation=60, horizontalalignment='right', fontsize=12)
p1 = patches.Rectangle((.51, -.02), width=.39, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
p2 = patches.Rectangle((.124, -.02), width=.386, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)
plt.savefig('./figs/damage_efficiency.png')
plt.show()
plt.close('all')


#elo system