# Standard package
import imp,sys,os,time

from SLURMWorker.SLURMWorker import SLURMWorker
from Core.mkdir_p import mkdir_p

cfgFileName             = sys.argv[1]
cfgAbsFilePath          = os.path.abspath(cfgFileName)
file                    = open( cfgFileName,'r')
cfg                     = imp.load_source( 'UFNTuple.__cfg_to_run__', cfgFileName, file)

commands = """
cd {base_path}
source setup_hpg.sh
UFNTuple {cfg_path}
""".format(
        base_path=os.environ["BASE_PATH"],
        cfg_path=cfgAbsFilePath,
        )

script_file_name = os.path.join(cfg.outputInfo.outputDir,cfg.slurm_job_name+".cfg")
mkdir_p(cfg.outputInfo.outputDir)
worker = SLURMWorker()
worker.make_sbatch_script(
        script_file_name,
        cfg.slurm_job_name,
        cfg.slurm_email,
        cfg.slurm_ntasks,
        cfg.slurm_mem,
        cfg.slurm_time,
        cfg.outputInfo.outputDir,
        commands,
        n_core = cfg.nCores,
        )
worker.sbatch_submit(script_file_name)
