for i in {1..1}; do
    #  learning_rate = sys.argv[1]
    #  reward_decay = sys.argv[2]
    #  INTERVAL = sys.argv[3]
    python3 Main.py 0.01 0.9 100 &
    python3 Main.py 0.01 0.9 50 &
    python3 Main.py 0.01 0.9 25 &
    python3 Main.py 0.01 0.8 100 &
    python3 Main.py 0.01 0.8 50 &
    python3 Main.py 0.01 0.8 25 &
    python3 Main.py 0.01 0.7 100 &
    python3 Main.py 0.01 0.7 50 &
    python3 Main.py 0.01 0.7 25
    wait
done

for i in {1..1}; do
    #  learning_rate = sys.argv[1]
    #  reward_decay = sys.argv[2]
    #  INTERVAL = sys.argv[3]
    python3 Main.py 0.05 0.9 100 &
    python3 Main.py 0.05 0.9 50 &
    python3 Main.py 0.05 0.9 25 &
    python3 Main.py 0.05 0.8 100 &
    python3 Main.py 0.05 0.8 50 &
    python3 Main.py 0.05 0.8 25 &
    python3 Main.py 0.05 0.7 100 &
    python3 Main.py 0.05 0.7 50 &
    python3 Main.py 0.05 0.7 25
    wait
done

for i in {1..1}; do
    #  learning_rate = sys.argv[1]
    #  reward_decay = sys.argv[2]
    #  INTERVAL = sys.argv[3]
    python3 Main.py 0.5 0.9 100 &
    python3 Main.py 0.5 0.9 50 &
    python3 Main.py 0.5 0.9 25 &
    python3 Main.py 0.5 0.8 100 &
    python3 Main.py 0.5 0.8 50 &
    python3 Main.py 0.5 0.8 25 &
    python3 Main.py 0.5 0.7 100 &
    python3 Main.py 0.5 0.7 50 &
    python3 Main.py 0.5 0.7 25
    wait
done

for i in {1..1}; do
    #  learning_rate = sys.argv[1]
    #  reward_decay = sys.argv[2]
    #  INTERVAL = sys.argv[3]
    python3 Main.py 0.5 0.9 100 &
    python3 Main.py 0.5 0.9 50 &
    python3 Main.py 0.5 0.9 25 &
    python3 Main.py 0.5 0.8 100 &
    python3 Main.py 0.5 0.8 50 &
    python3 Main.py 0.5 0.8 25 &
    python3 Main.py 0.5 0.7 100 &
    python3 Main.py 0.5 0.7 50 &
    python3 Main.py 0.5 0.7 25
    wait
done

echo "finish"
