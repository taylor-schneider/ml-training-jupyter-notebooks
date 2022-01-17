import time
import multiprocessing
import multiprocessing.pool
from tqdm.notebook import tqdm

# This class will keep track of exceptions raised in multithreaded functions if the user
# has elected to do so when they create the EnhancedThreadPool

class EnhancedThreadPoolException(Exception):
    def __init__(self, function, parameters, root_exeption, message):
        self.functiom=function
        self.parameters=parameters
        self.__cause__=root_exeption
        super().__init__(message)

# This class will act as an enhanced threadpool
# Ideally i would extend the ThreadPool class but I do not have enough time to impliment 
# ALL the required functionality. As such it will remain a separate class until I can extend.

class EnhancedThreadPool():

    def __init__(self, num_workers=4, handle_exceptions=True):
        
        self.handle_exceptions = handle_exceptions
        
        # Create a pointer for a progress bar to track progress
        self.progress_bar = None
        
        # Create a lock to manage internal access to the progress bar
        self.lock = multiprocessing.Lock()
        
        # Create internal pool to manage processes
        self.pool = multiprocessing.pool.ThreadPool(processes=num_workers)
        
        # Create a shared memory object to store the number of completed threads
        # between the various threads running in parallel
        self.shared_memory_buffer = multiprocessing.Value('i', 0)

    def _create_progress_bar(self, num_ops):
        
        return tqdm(range(num_ops))
        
    def _update_progress_bar(self, i):
        
        self.progress_bar.last_print_n = i
        self.progress_bar.n = i
        self.progress_bar.set_description(f'Completed Ops')
        self.progress_bar.refresh()

    # To make things simple we will define an internal function to hide the details
    # of the progress bar. This way the user can wwrite functions without worrying
    # about updating or locking the progress bar.
    @staticmethod
    def _wrapper_function(func, args, kwargs, internal_params):
        
        # Extract internal arguments for the manager's internal functions
        internal_args, internal_kwargs = internal_params
        lock, shared_memory_buffer = internal_args
        handle_exceptions = internal_kwargs["handle_exceptions"]
        
        # Run the user specificed function and return the results
        # Handle the exceptions is the user has requested us to do so
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if handle_exceptions:
                return EnhancedThreadPoolException(func, (args,kwargs), e, "An error ocurred while running the parallel function")
            else:
                raise
        finally:
            # Update the buffer for the progress bar to indicate the function has completed
            lock.acquire()
            shared_memory_buffer.value = shared_memory_buffer.value + 1
            lock.release()
        
    # This function will run a set of functions in separate processes.
    # The main thread will block and update a progress bar as the functions complete
    # It will return a result set once all the processes have finished or an
    # error has been encountered.
    # This function will run a set of functions in separate processes.
    # The main thread will block and update a progress bar as the functions complete
    # It will return a result set once all the processes have finished or an
    # error has been encountered.
    def parralelize(self, func, arg_set, kwarg_set):
        
        # Setup vars to help kick off parallelization
        num_ops = len(arg_set)
        self.progress_bar = self._create_progress_bar(num_ops)
        self.shared_memory_buffer.value = 0
        
        # Configure the parameters for the parallelization
        func_set = [func for i in range(0, num_ops)]
        internal_param_set = [
            ([self.lock, self.shared_memory_buffer], 
             {"handle_exceptions": self.handle_exceptions}
            ) for i in range(0, num_ops)]   
        param_set = zip(func_set, arg_set, kwarg_set, internal_param_set)
        
        # Start the functions in separate parallel processes and don't block
        apply_result = self.pool.starmap_async(self._wrapper_function, param_set)
        
        # Wait for the proceses to finish while updating the progress bar
        while not apply_result.ready():
            self._update_progress_bar(self.shared_memory_buffer.value)
            time.sleep(0.5)
        self._update_progress_bar(self.shared_memory_buffer.value)

        # Return the results
        return apply_result.get()
    
# This class will keep track of exceptions raised in multitprocess functions if the user
# has elected to do so when they create the EnhancedThreadPool

class EnhancedProcessPoolException(Exception):
    
    def __init__(self, message):
        super().__init__(message)
    def __init__(self, function, parameters, root_exeption, message):
        self.functiom=function
        self.parameters=parameters
        self.__cause__=root_exeption
        self.message = message

# This class will act as an enhanced threadpool
# Ideally i would extend the ThreadPool class but I do not have enough time to impliment 
# ALL the required functionality. As such it will remain a separate class until I can extend.

class EnhancedProcessPool():

    def __init__(self, num_workers=4, handle_exceptions=True, shared_memory="epp"):
        
        self.handle_exceptions = handle_exceptions
        
        # Create a pointer for a progress bar to track progress
        self.progress_bar = None
        
        # Create a lock to manage internal access to the progress bar
        self.manager = multiprocessing.Manager()
        self.lock = self.manager.Lock()
        
        # Create internal pool to manage processes
        self.pool = multiprocessing.Pool(processes=num_workers)
        
        # Create a shared memory object to store the number of completed threads
        # between the various threads running in parallel
        self.shared_memory_name = shared_memory
        try:
            self.shared_memory = multiprocessing.shared_memory.SharedMemory(name=self.shared_memory_name, create=True, size=1)
        except FileExistsError as fee:
            self.shared_memory = multiprocessing.shared_memory.SharedMemory(name=self.shared_memory_name, create=False, size=1)
        self.shared_memory_buffer = self.shared_memory.buf
        self.shared_memory_buffer[0] = 0

    def _create_progress_bar(self, num_ops):
        
        return tqdm(range(num_ops))
        
    def _update_progress_bar(self, i):
        
        self.progress_bar.last_print_n = i
        self.progress_bar.n = i
        self.progress_bar.set_description(f'Completed Ops')
        self.progress_bar.refresh()

    # To make things simple we will define an internal function to hide the details
    # of the progress bar. This way the user can wwrite functions without worrying
    # about updating or locking the progress bar.
    @staticmethod
    def _wrapper_function(func, args, kwargs, internal_params):
        
        # Extract internal arguments for the manager's internal functions
        internal_args, internal_kwargs = internal_params
        lock, shared_memory_name = internal_args
        handle_exceptions = internal_kwargs["handle_exceptions"]
        
        # Create pointer to shared memory (so we can update the progress bar)
        sm = multiprocessing.shared_memory.SharedMemory(name=shared_memory_name, create=False, size=1)
        smb = sm.buf
        
        # Run the user specificed function and return the results
        # Handle the exceptions is the user has requested us to do so
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if handle_exceptions:
                return EnhancedProcessPoolException(func, (args,kwargs), e, "An error ocurred while running the parallel function")
            else:
                raise
        finally:
            # Update the buffer for the progress bar to indicate the function has completed
            lock.acquire()
            smb[0] = int(smb[0]) + 1
            lock.release()
            sm.close()
        
    # This function will run a set of functions in separate processes.
    # The main thread will block and update a progress bar as the functions complete
    # It will return a result set once all the processes have finished or an
    # error has been encountered.
    # This function will run a set of functions in separate processes.
    # The main thread will block and update a progress bar as the functions complete
    # It will return a result set once all the processes have finished or an
    # error has been encountered.
    def parralelize(self, func, arg_set, kwarg_set):
        
        # Setup vars to help kick off parallelization
        num_ops = len(arg_set)
        self.progress_bar = self._create_progress_bar(num_ops)
        self.shared_memory_buffer[0] = 0
        
        # Configure the parameters for the parallelization
        func_set = [func for i in range(0, num_ops)]
        internal_param_set = [
            ([self.lock, self.shared_memory_name], 
             {"handle_exceptions": self.handle_exceptions}
            ) for i in range(0, num_ops)]   
        param_set = zip(func_set, arg_set, kwarg_set, internal_param_set)
        
        # Start the functions in separate parallel processes and don't block
        apply_result = self.pool.starmap_async(self._wrapper_function, param_set)
        
        # Wait for the proceses to finish while updating the progress bar
        while not apply_result.ready():
            self._update_progress_bar(self.shared_memory_buffer[0])
            time.sleep(0.5)
        self._update_progress_bar(self.shared_memory_buffer[0])
        
        # Cleanup
        self.shared_memory.close()
        self.shared_memory.unlink()

        # Return the results
        return apply_result.get()