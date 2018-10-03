#!/usr/bin/env python
import click
import tmuxcluster.tmux as tx


@click.group()
def main():
    pass


@main.command()
@click.argument('node')
@click.option('--delete', is_flag=True)
def make_job(node, delete):
    run = tx.Run(name='test_run', job_node=node)

    job1_task1 = 'ls /home'
    job1_task2 = 'cat /etc/hostname'
    if delete:
        run.make_job(job_name='test_job', task_scripts=[job1_task1, job1_task2], run=False)
        run.kill_jobs()
    else:
        run.make_job(job_name='test_job', task_scripts=[job1_task1, job1_task2])


@main.command()
@click.argument('node')
@click.option('--delete', is_flag=True)
def make_job1(node, delete):
    run = tx.Run(name='test_run', job_node=node)

    job1_task1 = 'sleep 30'
    job1_task2 = 'sleep 60'
    run.make_job(job_name='test_job1', task_scripts=[job1_task1, job1_task2])
    if delete:
        run.make_job(job_name='test_job1', task_scripts=[job1_task1, job1_task2], run=False)
        run.kill_jobs()
    else:
        run.make_job(job_name='test_job1', task_scripts=[job1_task1, job1_task2], run=True)


if __name__ == '__main__':
    main()
