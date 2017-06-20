for i in {1..3}; do
    #  learning_rate = sys.argv[1]
    #  reward_decay = sys.argv[2]
    #  INTERVAL = sys.argv[3]
    python3 Main.py 0.01 0.5 100 100 &
    python3 Main.py 0.01 0.5 100 200 &
    python3 Main.py 0.01 0.5 100 500
done


echo "finish"