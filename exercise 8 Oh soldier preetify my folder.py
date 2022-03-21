import os



def change_path(path,fileName,type) :
    print( "Current working directory before" )
    print( os.getcwd( ) )
    print( )
    os.chdir( path )
    print(f"new working directiory { os.getcwd( ) }")
    popo=os.listdir(path)
    print(f"hrer is the obj present in the directory",list)
    # file = open( fileName , 'r' )
    with open (fileName,'r') as file:
        file1=file.read()
        j=0
        for i in popo:
            if i.split(".")[0] in file1.split():
                continue
            elif  i.split(".")[1]==type:
                os.rename( i , str( j + 1 ) + type )
                j+=1
            else:
                os.rename( i , i.title( ) )

# ,text_file,format


change_path("D:\PIctures\Quotes" , "quotes.txt" , "jpg" )