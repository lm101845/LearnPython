import subprocess
import time


def start_mongodb():
    mongod_path = "D:\\sortware\\42-mogodb\\content\\bin\\mongod.exe"  # MongoDB可执行文件路径
    data_path = "D:\\sortware\\42-mogodb\\content\\data\\db"  # MongoDB数据路径
    log_path = "D:\\sortware\\42-mogodb\\content\\data\\log\\mongod.log"  # MongoDB日志路径

    try:
        # 构建MongoDB启动命令
        cmd = [mongod_path, "--dbpath", data_path, "--logpath", log_path]
        # 启动MongoDB服务
        subprocess.Popen(cmd)
        print("MongoDB started.")
    except Exception as e:
        print(f"Error starting MongoDB: {e}")


def start_redis():
    redis_server_path = "D:\\sortware\\43-redis\\redis\\content\\redis-server.exe"  # Redis可执行文件路径
    redis_conf_path = "D:\\sortware\\43-redis\\redis\\content\\redis.windows.conf"  # 假设Redis配置文件在此路径

    try:
        # 启动Redis服务，这里假设你有一个redis.conf配置文件
        cmd = [redis_server_path, redis_conf_path]
        subprocess.Popen(cmd)
        print("Redis started.")
    except Exception as e:
        print(f"Error starting Redis: {e}")


if __name__ == "__main__":
    start_mongodb()
    start_redis()
    # 等待一段时间以确保服务已成功启动
    time.sleep(5)
    print("MongoDB and Redis should be running now.")
    # 在这里添加你的代码