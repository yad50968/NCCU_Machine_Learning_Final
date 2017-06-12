from DQN_brain import DeepQNetwork
import psycopg2
import random
import numpy as np


def query_etf_data_and_price():
    conn = psycopg2.connect(host="",
                            dbname="",
                            user="",
                            password="",
                            port="")
    cur = conn.cursor()

    etf_data_query = """
            SELECT a.dif, b.ema, c.macd, d.obv, e.psy, f.rsi
            FROM etf_dif a
            LEFT JOIN etf_ema b
            ON a.etf_id = b.etf_id AND a.date = b.date AND b.param = 'ema50'
            LEFT JOIN etf_macd c
            ON a.etf_id = c.etf_id AND a.date = c.date
            LEFT JOIN etf_obv d
            ON a.etf_id = d.etf_id AND a.date = d.date
            LEFT JOIN etf_psy e
            ON a.etf_id = e.etf_id AND a.date = e.date
            LEFT JOIN etf_rsi f
            ON a.etf_id = f.etf_id AND a.date = f.date AND f.param = '50'
            WHERE a.etf_id = 1 AND a.date>2999
            ORDER by a.date
            """

    cur.execute(etf_data_query)
    etf_data = np.array(cur.fetchall())

    
    price_query = """
                SELECT close 
                FROM etf_data 
                WHERE date > 2999 AND date < 4351 AND etf_id = 1 
                ORDER BY date ASC
           """

    cur.execute(price_query)
    price_data = np.array(cur.fetchall())

    cur.close()
    conn.close()

    return (etf_data, price_data)


def observe_r_update(action, day, keeping_table, price_data, FEE=0.01):
    if action == 0:
        r = sell_1(day, keeping_table, price_data) - FEE
    elif action == 2:
        r = buy_1(day, keeping_table, price_data) - FEE
    else:
        r = 0         # action==1 r=0
    return r

def sell_1(day, keeping_table, price_data):
    if keeping_table[0] == 0:
        keeping_table[1] += 1
        keeping_table[2] += price_data[day+1]
        return 0
    else:
        r = price_data[ day+1] - keeping_table[2] / keeping_table[0]
        keeping_table[2] -= keeping_table[2] / keeping_table[0]
        keeping_table[0] -= 1
        return r
# 買


def buy_1(day, keeping_table, price_data):
    if keeping_table[1] == 0:
        keeping_table[0] += 1
        keeping_table[2] += price_data[day+1]
        return 0
    else:
        r = keeping_table[2] / keeping_table[1] - price_data[day+1]
        keeping_table[2] -= keeping_table[2] / keeping_table[1]
        keeping_table[1] -= 1
        return r

def run_testing(RL):
    
    total_reward = 0
    day = 0
    
    TRAINING_DAYS = 900
    INTERVAL = 100

    etf_data, price_data = query_etf_data_and_price()
    price_data = price_data.T.flatten()[: TRAINING_DAYS]
    #etf_data = np.random.randint(100, size=(100, 6))
    #price_data = np.random.randint(100, size=(100))

    price_data_size_minus1 = price_data.size - 1
    keeping_table = np.zeros(3)
    
    
    for i in range(3):
        keeping_table[i] = 0
        
    observation = etf_data[day]

    for i in range(INTERVAL):
          
        # RL choose action based on observation
        action = RL.choose_action(observation)

        # RL take action and get next observation and reward
        
        if day != price_data_size_minus1:
            observation_ = etf_data[day+1]
        else:
            observation_ = observation
                
        reward = observe_r_update(action, day, keeping_table, price_data)
        total_reward += reward
            

        # swap observation
        observation = observation_

        # break while loop when end of this episode
        day += 1
        
    return total_reward

def run_learning(RL):
    
    TRAINING_DAYS = 900
    INTERVAL = 100

    etf_data, price_data = query_etf_data_and_price()
    price_data = price_data.T.flatten()[: TRAINING_DAYS]
    #etf_data = np.random.randint(100, size=(1000, 6))
    #price_data = np.random.randint(100, size=(1000))

    price_data_size_minus1 =  price_data.size - 1
    keeping_table = np.zeros(3)
    step = 0

    for episode in range(350):
        # initial observation
        for i in range(3):
            keeping_table[i] = 0
        day = random.randint(1, TRAINING_DAYS - INTERVAL) - 1
        observation = etf_data[day]

        for i in range(INTERVAL):
          
            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            
            if day != price_data_size_minus1:
                observation_ = etf_data[day+1]
            else:
                observation_ = observation
                
            reward = observe_r_update(action, day, keeping_table, price_data)
            RL.store_transition(observation, action, reward, observation_)

            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            
            step += 1
            day += 1


if __name__ == "__main__":
   
    RL = DeepQNetwork(n_actions=3,
                      n_features=6,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=2000,
                      output_graph=True
                      )
    run_learning(RL)
    value = run_testing(RL)
    print(value)
    RL.plot_cost()
  