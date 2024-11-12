import React from 'react'

export default function Home() {
    return (
        
        <div className="mx-auto w-full max-w-7xl">
            <aside className="relative overflow-hidden text-black rounded-lg sm:mx-16 mx-2 sm:py-16">
       
                        <div className="relative z-10 max-w-screen-xl px-4  pb-20 pt-10 sm:py-24 mx-auto sm:px-6 lg:px-8">
                            <div className="max-w-xl sm:mt-1 mt-80 space-y-8 text-center sm:text-right sm:ml-auto">
                    
                                    <h2 className="text-2xl mb-20 font-bold sm:text-2xl">
                                        Learning Management System
                                        <span className="hidden sm:block text-4xl">Welcome!</span>
                                    </h2>
                            </div>
                        </div>
                        
                        <div className="absolute inset-0 w-full sm:my-20 sm:pt-10 pt-12 h-full ">
                        <img className="w-100" src="./images/bgiamge.png" alt="image1" />
                        </div>
                     

            </aside>
             
    
        </div>
    );
}