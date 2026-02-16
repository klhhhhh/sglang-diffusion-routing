import argparse
from .launcher import launch_cluster
from .router.diffusion_router import main as run_router_main  # miles#544 的 router 里最好提供 main()

def main():
    ap = argparse.ArgumentParser(prog="sglang-d-router")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("run-router", help="Run the diffusion router only.")
    p1.add_argument("--host", default="0.0.0.0")
    p1.add_argument("--port", type=int, default=30080)
    p1.add_argument("--algorithm", default="least-request",
                    choices=["least-request", "round-robin", "random"])
    p1.add_argument("--max-connections", type=int, default=256)
    p1.add_argument("--timeout-secs", type=float, default=300.0)
    p1.add_argument("--health-check-interval-secs", type=float, default=10.0)
    p1.add_argument("--health-check-failure-threshold", type=int, default=3)

    p2 = sub.add_parser("launch", help="Launch N sglang diffusion workers + router, and auto-register workers.")
    p2.add_argument("--model-path", required=True)
    p2.add_argument("--num-workers", type=int, default=2)
    p2.add_argument("--base-port", type=int, default=30010)
    p2.add_argument("--router-port", type=int, default=30080)
    p2.add_argument("--gpus", default="", help='Comma-separated GPU ids, e.g. "0,1,2,3". If empty, do not set CUDA_VISIBLE_DEVICES.')
    p2.add_argument("--extra-serve-args", default="", help='Extra args passed to `sglang serve`, e.g. \'--text-encoder-cpu-offload --pin-cpu-memory\'')

    args = ap.parse_args()

    if args.cmd == "run-router":
        run_router_main(
            host=args.host,
            port=args.port,
            algorithm=args.algorithm,
            max_connections=args.max_connections,
            timeout_secs=args.timeout_secs,
            health_check_interval_secs=args.health_check_interval_secs,
            health_check_failure_threshold=args.health_check_failure_threshold,
        )
    else:
        launch_cluster(
            model_path=args.model_path,
            num_workers=args.num_workers,
            base_port=args.base_port,
            router_port=args.router_port,
            gpus=args.gpus,
            extra_serve_args=args.extra_serve_args,
        )
