from consts import *



def MPI_Initialized(startwall, dt):
    out  = 'MPI_Initialized entering at walltime {:.9f}, cputime {:.9f} seconds in thread 0.\n'.format(startwall, dt); startwall += dt
    out += 'int result=0\n'.format()
    out += 'MPI_Initialized returning at walltime {:.9f}, cputime {:.9f} seconds in thread 0.'.format(startwall, dt); startwall += dt
    return out, startwall

def MPI_Init(startwall, dt):
    out  = 'MPI_Init entering at walltime {:.9f}, cputime {:.9f} seconds in thread 0.\n'.format(startwall, dt); startwall += dt
    out += 'int argc=0\n'.format()
    out += 'string argv[0]=<IGNORED>\n'.format()
    out += 'MPI_Init returning at walltime {:.9f}, cputime {:.9f} seconds in thread 0.'.format(startwall, dt); startwall += dt
    return out, startwall

def MPI_Comm_rank(rank, comm, startwall, dt):
    out  = 'MPI_Comm_rank entering at walltime {:.9f}, cputime {:.9f} seconds in thread 0.\n'.format(startwall, dt); startwall += dt
    out += 'MPI_Comm comm={} ({})\n'.format(comm, num_communicator[comm])
    out += 'int rank={}\n'.format(rank)
    out += 'MPI_Comm_rank returning at walltime {:.9f}, cputime {:.9f} seconds in thread 0.'.format(startwall, dt); startwall += dt
    return out, startwall

def MPI_Comm_size(comm, world_size, startwall, dt):
    out  = 'MPI_Comm_size entering at walltime {:.9f}, cputime {:.9f} seconds in thread 0.\n'.format(startwall, dt); startwall += dt
    out += 'MPI_Comm comm={} ({})\n'.format(comm, num_communicator[comm])
    out += 'int size={}\n'.format(world_size)
    out += 'MPI_Comm_size returning at walltime {:.9f}, cputime {:.9f} seconds in thread 0.'.format(startwall, dt); startwall += dt
    return out, startwall + dt

def MPI_Finalize(end, final_dt):
    out  = "MPI_Finalize entering at walltime {:.9f}, cputime {:.9f} seconds in thread 0.\n".format(end, final_dt); end += final_dt
    out += "MPI_Finalize returning at walltime {:.9f}, cputime {:.9f} seconds in thread 0.".format(end, final_dt);
    return out, None

def MPI_Send(startwall, startcpu, count, type, dst, tag, comm, endwall, endcpu, thread = 0):
    return '\n'.join([
                        'MPI_Send entering at walltime {:.9f}, cputime {:.9f} seconds in thread {}.'.format(startwall, startcpu, thread),
                        'int count={}'.format(count),
                        'MPI_Datatype datatype={} ({})'.format(type, num_datatype[type]),
                        'int dest={}'.format(dst),
                        'int tag={}'.format(tag),
                        'MPI_Comm comm={} ({})'.format(comm, num_communicator[comm]),
                        'MPI_Send returning at walltime {:.9f}, cputime {:.9f} seconds in thread {}.'.format(endwall, endcpu, thread)
                     ]), endwall + endcpu

def MPI_Irecv(startwall, startcpu, count, type, src, tag, comm, endwall, endcpu, thread = 0):
    return '\n'.join([
                        'MPI_Irecv entering at walltime {:.9f}, cputime {:.9f} seconds in thread {}.'.format(startwall, startcpu, thread),
                        'int count={}'.format(count),
                        'MPI_Datatype datatype={} ({})'.format(type, num_datatype[type]),
                        'int source={}'.format(src),
                        'int tag={}'.format(tag),
                        'MPI_Comm comm={} ({})'.format(comm, num_communicator[comm]),
                        'MPI_Request request=[2]',
                        'MPI_Irecv returning at walltime {:.9f}, cputime {:.9f} seconds in thread {}.'.format(endwall, endcpu, thread)
                    ]), endwall + endcpu

def MPI_Wait(startwall, startcpu, count, type, src, tag, comm, endwall, endcpu, thread = 0):
    size = 1

    if (num_datatype[type] == "MPI_INT"):
        size = 4
    elif (num_datatype[type] == "MPI_DOUBLE"):
        size = 1

    return '\n'.join([
                        'MPI_Wait entering at walltime {:.9f}, cputime {:.9f} seconds in thread {}.'.format(startwall, startcpu, thread),
                        'MPI_Request request=[{}]'.format(2),
                        "MPI_Status status=[{{bytes={}, cancelled={}, source={}, tag={}, error={}}}]".format(count*size, 0, src, tag, 0),
                        'MPI_Wait returning at walltime {:.9f}, cputime {:.9f} seconds in thread {}.'.format(endwall, endcpu, thread)
                    ]), endwall + endcpu

def MPI_Alltoall(startwall, startcpu, count, type, tag, comm, endwall, endcpu, thread = 0):
    return '\n'.join([
                        'MPI_Alltoall entering at walltime {:.9f}, cputime {:.9f} seconds in thread {}.'.format(startwall, startcpu, thread),
                        'int sendcount={}'.format(count),
                        'MPI_Datatype sendtype={} ({})'.format(type, num_datatype[type]),
                        'int recvcount={}'.format(count),
                        'MPI_Datatype recvtype={} ({})'.format(type, num_datatype[type]),
                        'MPI_Comm comm={} ({})'.format(comm, num_communicator[comm]),
                        'MPI_Alltoall returning at walltime {:.9f}, cputime {:.9f} seconds in thread {}.'.format(endwall, endcpu, thread)
                    ]), endwall + endcpu
