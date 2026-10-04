# Deployment strategies

**Domain:** system design, with overlap into DevOps and release engineering.

**Status:** conceptual guide and learning roadmap available. Deployment labs and a hosted Treasure Hunt are not implemented.

部署策略讨论新版本如何上线、如何判断是否正常，以及出问题如何恢复。本节已有讲解和路线图，还没有部署实验或在线游戏。

## What we have today

Repository inventory checked on 5 October 2026. This describes files in this repository, not infrastructure outside it.

| Capability | Evidence | What it means |
| --- | --- | --- |
| Original terminal game | [01 — Foundations](../../projects/treasure-hunt/python/01-foundations/README.md) | Runs locally with Python 3 |
| Input validation and helper functions | [02 — Functions and validation](../../projects/treasure-hunt/python/02-functions-and-validation/README.md) | A second complete local version |
| Inventory, progress and rewards | [03 — Collections and progress](../../projects/treasure-hunt/python/03-collections-and-progress/README.md) | A third complete local version |
| Gameplay regression tests | [Stage 3 tests](../../projects/treasure-hunt/python/03-collections-and-progress/test_game.py) | Check game behavior, not HTTP traffic or deployments |
| Version history and run instructions | Git and project READMEs | We can identify and compare source versions |
| Browser UI, HTTP API, persistent game sessions | Not implemented | The game uses terminal input and process memory |
| Deployment configuration, hosting setup, CI/CD workflow | Not present in this repository | There is no automated build-and-release path here |

目前是本地终端游戏：关掉进程，游戏状态就结束。推送代码到 GitHub 并不等于把游戏部署成在线服务。

## Vocabulary before strategies

- **Deployment:** put a version into a target environment and run it there. 部署：把某个版本放到目标环境运行。
- **Release:** make a capability available to users. Deployment and release can be separate, for example through a feature flag. 发布：让用户开始使用某功能。
- **Instance:** one running copy of the application. 实例：正在运行的一份程序。
- **Traffic:** requests arriving from users. 流量：用户发来的请求。
- **Rollback:** restore service using an earlier application version or routing configuration. 回退：切回旧版或旧流量配置。
- **CI/CD:** automated checks and delivery steps; continuous delivery can include a manual production gate, while continuous deployment automates that promotion. 持续集成检查代码，交付流程把已验证的版本送到目标环境。

The same Python game can be distributed as a download without a server. The strategies below concern the planned online service, where users may be playing during an update.

## Compare four strategies

| Strategy | How it changes versions | Main tradeoff |
| --- | --- | --- |
| Recreate | Stop the old instances, then start the new ones | Simple, but normally includes an outage |
| Rolling update | Replace instances in batches | Needs enough healthy capacity; old and new versions coexist |
| Blue-green | Prepare another environment and switch traffic to it | Fast traffic reversal can be possible, but duplicate capacity costs more |
| Canary | Give the new version a small audience before expanding | Limits initial exposure, but needs useful measurements and controlled routing |

Recreate and rolling behavior are described in the [Kubernetes rolling-update guide](https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/). Blue-green and canary tradeoffs are described in [AWS deployment strategies](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html). These are concepts we can study without choosing either platform.

Blue-green describes environments; canary describes gradual exposure. They can be combined. A strategy alone does not guarantee zero downtime or preserved player sessions.

蓝绿强调两套环境，金丝雀强调先让小部分用户使用新版，两者可以结合。部署策略本身不保证不中断，也不自动保存玩家进度。

## One shared example: update Treasure Hunt

The following is a proposed exercise, not existing web functionality. Imagine version A is serving a browser game and version B adds a new treasure room.

- **Recreate:** announce a maintenance period, stop A, start B, and verify a game can be created and completed. A failed start requires restoring A.
- **Rolling:** replace one service instance at a time. Check whether a player can send consecutive moves to different versions without losing progress.
- **Blue-green:** test B through a separate route before switching the public route. Keep A available until the observation period ends.
- **Canary:** keep most sessions on A and assign a small group to B. Compare failed moves, response times, and game-state errors before increasing exposure. Percentages and observation periods are exercise choices, not universal defaults.

For a game, routing by a stable session cohort is often easier to reason about than randomly changing version on each move. It still needs compatible shared state or a deliberate session-migration policy.

同一玩家连续操作时，不能随便在不兼容的版本间跳来跳去。固定分组有帮助，但不能代替存档和兼容性设计。

## What we should build, gradually

This is the proposed sequence for future labs. No cloud service or container platform is required to begin learning.

| Stage | Deliverable | Done when |
| --- | --- | --- |
| 1. Understand the current app | Run a game and identify code versus in-memory state | Explain what is lost when the process ends |
| 2. Make a local web service | Separate game rules from terminal input; add create-game, move and state operations with a minimal browser UI | Two independent sessions can play without changing each other's state |
| 3. Make releases repeatable | Record a version ID, Python/runtime requirements, dependencies, configuration and startup command; retain an older artifact | The same release starts consistently and the prior release can be restored |
| 4. Practise recreate locally | Start A, stop it, start B, verify, then restore A | Measure the outage and explain what happens to ongoing games |
| 5. Support multiple instances | Add session storage/policy, readiness checks, graceful shutdown, routing and compatibility tests | An update preserves the intended game behavior across instances |
| 6. Practise gradual deployment | Demonstrate rolling, blue-green and canary separately | A deliberately faulty B is detected and traffic safely returns to A |
| 7. Automate delivery | Add CI checks, artifact creation, environment configuration and a release/rollback procedure | A failed check blocks promotion and a release can be traced to its source |

Containers are an optional packaging choice. Kubernetes is not a prerequisite for these lessons. Hosting selection comes after we have a working service and know its requirements.

## What to check before a shared hosted demo

These are readiness requirements for the proposed service, not features already implemented.

- **State:** choose whether sessions may reset or must survive restarts. If preservation is required, store them outside a replaceable process and test concurrent updates.
- **Health:** distinguish a running process from one ready to handle requests. Check an actual create-game/move/read-state flow as well as the readiness signal.
- **Shutdown:** stop sending new work to retiring instances and allow in-flight requests to finish within a defined limit.
- **Evidence:** record version, request errors, latency and gameplay failures. Decide the observation period and promotion/stop criteria before shifting traffic.
- **Access and configuration:** isolate each player's session, validate moves on the server, and keep environment credentials out of source control.
- **Recovery:** retain the previous release and configuration. Test that it still understands data written by the new version.

### Rollback is not undo for data

Suppose B changes the saved inventory format and A cannot read it. Switching traffic back to A will not repair the saves. Plan compatible schema changes, a migration/recovery procedure, and backups where persistent data matters. Restoring a backup can discard newer progress, so it is a separate decision from restoring code.

回退代码不会自动撤销数据变化。新版写出的存档，旧版必须能读取，或者要有明确的数据恢复方案。

## Learning checks

- [ ] Explain why publishing repository code is different from deploying a service.
- [ ] Sketch where versions A and B run in each strategy.
- [ ] Explain what a player experiences if an update happens mid-game.
- [ ] Identify what we would measure before promoting a canary.
- [ ] Explain why healthy servers do not guarantee correct gameplay.
- [ ] Describe a case where switching back to old code does not recover data.

**Next practical milestone:** a local web version with independent sessions. Keep its runnable implementation under `projects/treasure-hunt/`; link the deployment lab here when it exists. Existing Python learning stages remain standalone snapshots.

[System design](../README.md) · [Treasure Hunt](../../projects/treasure-hunt/README.md)
