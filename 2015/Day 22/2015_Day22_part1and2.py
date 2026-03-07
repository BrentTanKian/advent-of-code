import heapq


def turn_step(current_state_dict, spell):
    state = current_state_dict.copy()
    state['win_state'] = False
    state['lose_state'] = False

    # Include this block for part 2's solution and omit for part 1's solution
    if state['is_player_turn']:
        state['player_hp'] -= 1
        if state['player_hp'] <= 0:
            state['lose_state'] = True
            return state

    if state['shield_timer'] > 0:
        player_shield = 7
        state['shield_timer'] -= 1
    else:
        player_shield = 0
    if state['poison_timer'] > 0:
        state['boss_hp'] -= 3
        state['poison_timer'] -= 1
    if state['recharge_timer'] > 0:
        state['player_mana'] += 101
        state['recharge_timer'] -= 1
    #win lose check
    if state['boss_hp'] <= 0:
        state['win_state'] = True
        return state
    if state['is_player_turn']:
        if spell == 'Magic Missile':
            if state['player_mana'] < 53:
                return None
            else:
                state['boss_hp'] -= 4
                state['player_mana'] -= 53
        elif spell == 'Drain':
            if state['player_mana'] < 73:
                return None
            else:
                state['boss_hp'] -= 2
                state['player_hp'] += 2
                state['player_mana'] -= 73
        elif spell == 'Shield':
            if state['shield_timer'] > 0 or state['player_mana'] < 113:
                return None
            else:
                state['shield_timer'] = 6
                state['player_mana'] -= 113
        elif spell == 'Poison':
            if state['poison_timer'] > 0 or state['player_mana'] < 173:
                return None
            else:
                state['player_mana'] -= 173
                state['poison_timer'] = 6
        elif spell == 'Recharge':
            if state['recharge_timer'] > 0 or state['player_mana'] < 229:
                return None
            else:
                state['player_mana'] -= 229
                state['recharge_timer'] = 5
        else:
            return None
        if state['boss_hp'] <= 0:
            state['win_state'] = True
            return state
        state['is_player_turn'] = False
    else:
        dmg = max(1, state['boss_dmg'] - player_shield)
        state['player_hp'] -= dmg
        if state['player_hp'] <= 0:
            state['lose_state'] = True
            return state
        state['is_player_turn'] = True
    return state


if __name__ == "__main__":
    my_heap = []
    best_cost = {}
    spell_list = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']
    cost_map = {'Magic Missile': 53, 'Drain': 73, 'Shield': 113, 'Poison': 173, 'Recharge': 229}
    state = {'player_hp': 50,
            'player_mana': 500,
            'boss_hp': 58,
            'shield_timer': 0,
            'poison_timer': 0,
            'recharge_timer': 0,
            'is_player_turn': True,
            'boss_dmg': 9,
            'win_state': False,
            'lose_state': False}
    total_mana_spent, counter = 0, 0
    heapq.heappush(my_heap, (total_mana_spent, counter, state))
    while my_heap:
        cur_state = heapq.heappop(my_heap)
        total_mana_spent = cur_state[0]
        cur_state_dict = cur_state[2]
        if cur_state_dict['win_state'] == True:
            print('Win reached, total_mana_spent = ' + str(total_mana_spent))
            break
        elif cur_state_dict['lose_state'] == True:
            continue
        else:
            cur_tuple = (cur_state_dict['is_player_turn'],
                        cur_state_dict['player_hp'],
                        cur_state_dict['player_mana'],
                        cur_state_dict['boss_hp'],
                        cur_state_dict['shield_timer'],
                        cur_state_dict['poison_timer'],
                        cur_state_dict['recharge_timer'])
            if cur_tuple in best_cost and total_mana_spent >= best_cost[cur_tuple]:
                continue
            else:
                best_cost[cur_tuple] = total_mana_spent
                if cur_state_dict['is_player_turn'] == True:
                    for spell in spell_list:
                        new_state = turn_step(cur_state_dict, spell)
                        if new_state == None:
                            continue
                        else:
                            counter += 1
                            new_spent = total_mana_spent + cost_map[spell]
                            heapq.heappush(my_heap, (new_spent, counter, new_state))
                else:
                    new_state = turn_step(cur_state_dict, None)
                    if new_state != None:
                        counter += 1
                        heapq.heappush(my_heap, (total_mana_spent, counter, new_state))