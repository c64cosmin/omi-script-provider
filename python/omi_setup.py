from distutils.core import setup, Extension
from distutils import ccompiler
import os

curr_dir = os.path.abspath('..')
root_dir = os.path.abspath('../..')


lib_dir = None
config_mak = open (root_dir + '/omi/Unix/output/config.mak', 'r')
if config_mak is not None:
    for line in config_mak:
        if 0 == line.find ('CONFIG_LIBDIR='):
            lib_dir = line[14:].rstrip ()
            break

module1 = Extension (
    'omi',
    sources = ['bookend_wrapper.cpp',
               'client_wrapper.cpp',
               'functor.cpp',
               'mi_context_wrapper.cpp',
               'mi_function_table_placeholder.cpp',
               'mi_instance_wrapper.cpp',
               'mi_module_wrapper.cpp',
               'mi_schema_wrapper.cpp',
               'mi_wrapper.cpp',
               'omi_module.cpp',
               'py_converter.cpp',
               'shared.cpp'],
    include_dirs = [root_dir,
                    curr_dir + '/provider',
                    root_dir + '/omi/Unix/output/include',
                    root_dir + '/omi/Unix/common'],
    library_dirs = [curr_dir + '/bin'],
    
    runtime_library_dirs = [curr_dir + '/bin',
                            lib_dir],

    libraries = ['OMIScriptProvider'],
    define_macros = [('PRINT_BOOKENDS','0')],
    
    extra_link_args = ['-Wl,-R' + curr_dir + '/bin',
                       '-Wl,-R' + lib_dir],
    )

    
setup (name = 'omi',
       version = '1.0',
       description = 'The Python OMI interface',
       ext_modules = [module1],
       data_files = [(lib_dir, ['client.py'])],
       )
