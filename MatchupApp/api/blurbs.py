

def genBlurbs(allyStats, enemyStats, Role):
    blurbs = {
        'blurb1': '',
        'blurb2': '',
        'blurb3': '',
        'blurb4': ''
    }
    count = 1
    if allyStats['inRole'] == 0:
        blurbs['blurb'+str(count)] = 'Ally is playing out of role in this lane'
        count += 1
    if enemyStats['inRole'] == 0:
        blurbs['blurb'+str(count)] = 'Enemy is playing out of role in this lane'
        count += 1 
    
    if allyStats['OTP'] >= 2/3:
        blurbs['blurb'+str(count)] = 'Ally is a one trick pony on their champion'
        count += 1 
    if allyStats['OTP'] >= 2/3:
        blurbs['blurb'+str(count)] = 'Enemy is a one trick pony on their champion'
        count += 1 
    
    if count >= 4:
        return blurbs

    if Role == 'TOP':
        if enemyStats['SSD'] > 22:
            blurbs['blurb'+str(count)] = 'Enemy is skilled a kiting/dodging skill shots'
            count += 1
        if enemyStats['turretPlates'] >= allyStats['turretPlates']:
            blurbs['blurb'+str(count)] = 'Enemy destroys more turret plates on avg. and will stay in lane before 15 mins'
            count += 1
        else:
            blurbs['blurb'+str(count)] = 'Ally destroys more turret plates on avg. and will stay in lane before 15 mins'
            count += 1
        if enemyStats['firstTurret'] >= 2/3:
            blurbs['blurb'+str(count)] = 'Enemy is more likely to get first turret'
            count += 1
        elif allyStats['firstTurret'] >= 2/3:
            blurbs['blurb'+str(count)] = 'Ally is more likely to get first turret'
            count += 1
        if allyStats['csADV'] > enemyStats['csADV']+20:
            blurbs['blurb'+str(count)] = 'Ally expected to outfarm their lane opponent'
            count += 1
        elif enemyStats['csADV'] > allyStats['csADV']+20:
            blurbs['blurb'+str(count)] = 'Enemy expected to outfarm their lane opponent'
            count += 1
    elif Role == 'JUNGLE':
        if enemyStats['buffsStolen'] > 10:
            blurbs['blurb'+str(count)] = 'Enemy steals buffs from your team a lot'
            count += 1
        if allyStats['buffsStolen'] > 10:
            blurbs['blurb'+str(count)] = 'Ally steals buffs from enemy team a lot'
            count += 1
        if enemyStats['enemyJungleMonsterKills'] > 12:
            blurbs['blurb'+str(count)] = 'Enemy spends a lot of time invading your jungle'
            count += 1
        if allyStats['enemyJungleMonsterKills'] > 12:
            blurbs['blurb'+str(count)] = 'Ally spends a lot of time invading enemy jungle'
            count += 1
        if allyStats['csADV'] > enemyStats['csADV']+20:
            blurbs['blurb'+str(count)] = 'Ally commonly outfarms their lane opponent'
            count += 1
        elif enemyStats['csADV'] > allyStats['csADV']+20:
            blurbs['blurb'+str(count)] = 'Enemy commonly outfarms their lane opponent'
            count += 1
    elif Role == 'MIDDLE':
        if enemyStats['SSD'] > 25:
            blurbs['blurb'+str(count)] = 'Enemy is skilled a kiting/dodging skill shots'
            count += 1
        if enemyStats['turretPlates'] >= allyStats['turretPlates']:
            blurbs['blurb'+str(count)] = 'Enemy destroys more turret plates on avg. and will stay in lane before 15 mins'
            count += 1
        else:
            blurbs['blurb'+str(count)] = 'Ally destroys more turret plates on avg. and will stay in lane before 15 mins'
            count += 1
        if enemyStats['firstTurret'] >= 2/3:
            blurbs['blurb'+str(count)] = 'Enemy is more likely to get first turret'
            count += 1
        elif allyStats['firstTurret'] >= 2/3:
            blurbs['blurb'+str(count)] = 'Ally is more likely to get first turret'
            count += 1
        if allyStats['csADV'] > enemyStats['csADV']+20:
            blurbs['blurb'+str(count)] = 'Ally expected to outfarm their lane opponent'
            count += 1
        elif enemyStats['csADV'] > allyStats['csADV']+20:
            blurbs['blurb'+str(count)] = 'Enemy expected to outfarm their lane opponent'
            count += 1
    elif Role == 'BOTTOM':
        if enemyStats['SSD'] > 25:
            blurbs['blurb'+str(count)] = 'Enemy is skilled a kiting/dodging skill shots'
            count += 1
        if enemyStats['turretPlates'] >= allyStats['turretPlates']:
            blurbs['blurb'+str(count)] = 'Enemy destroys more turret plates on avg. and will stay in lane before 15 mins'
            count += 1
        else:
            blurbs['blurb'+str(count)] = 'Ally destroys more turret plates on avg. and will stay in lane before 15 mins'
            count += 1
        if enemyStats['firstTurret'] >= 2/3:
            blurbs['blurb'+str(count)] = 'Enemy is more likely to get first turret'
            count += 1
        elif allyStats['firstTurret'] >= 2/3:
            blurbs['blurb'+str(count)] = 'Ally is more likely to get first turret'
            count += 1
        if allyStats['csADV'] > enemyStats['csADV']+20:
            blurbs['blurb'+str(count)] = 'Ally expected to outfarm their lane opponent'
            count += 1
        elif enemyStats['csADV'] > allyStats['csADV']+20:
            blurbs['blurb'+str(count)] = 'Enemy expected to outfarm their lane opponent'
            count += 1
    else:
        if allyStats['questOT'] > 1/2:
            blurbs['blurb'+str(count)] = 'Ally expected to finish support quest on time'
            count += 1
        if enemyStats['questOT'] > 1/2:
            blurbs['blurb'+str(count)] = 'Ally expected to finish support quest on time'
            count += 1
        if enemyStats['SSD'] > 25:
            blurbs['blurb'+str(count)] = 'Enemy is skilled a kiting/dodging skill shots'
            count += 1
        if allyStats['landSS'] > 9:
            blurbs['blurb'+str(count)] = 'Ally lands most skill shot attempts'
            count += 1
        if enemyStats['landSS'] > 9:
            blurbs['blurb'+str(count)] = 'Enemy lands most skill shot attempts'
            count += 1
        if allyStats['saveAllyFromDeath'] >= 3:
            blurbs['blurb'+str(count)] = 'Ally is skilled at bailing out their teammates in fights'
            count += 1
        if enemyStats['saveAllyFromDeath'] >= 3:
            blurbs['blurb'+str(count)] = 'Enemy is skilled at bailing out their teammates in fights'
            count += 1
    if count == 1:
        blurbs['blurb1'] = "No noteworthy insights found for this lane/role"
    return blurbs