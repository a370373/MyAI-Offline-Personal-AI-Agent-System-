import subprocess


class ShellRuntime:


    def execute(self,cmd):

        try:

            result=subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True
            )


            return {

                "success":True,

                "stdout":result.stdout,

                "stderr":result.stderr

            }


        except Exception as e:

            return {

                "success":False,

                "error":str(e)

            }
