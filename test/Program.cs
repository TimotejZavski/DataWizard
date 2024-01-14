using Microsoft.AspNetCore.Hosting;
using System.Reflection.PortableExecutable;
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.Kestrel.Core;

namespace test;


public class Program
{

    public static void Main(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);

        //builder.Services.Configure<KestrelServerOptions>(options =>
        //{
        //    options.Limits.MaxRequestBodySize = null;
        //});

        //builder.WebHost.ConfigureKestrel(opt =>
        //{
        //    opt.Limits.MaxRequestBodySize = null;  //disable the request body limit.
        //});

        //builder.Services.Configure<FormOptions>(options =>
        //{
        //    options.ValueLengthLimit = int.MaxValue;
        //    options.MultipartBodyLengthLimit = int.MaxValue;
        //});

        // Add services to the container.
        builder.Services.AddRazorPages();

        var app = builder.Build();

        // Configure the HTTP request pipeline.
        if (!app.Environment.IsDevelopment())
        {
            app.UseExceptionHandler("/Error");
            // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
            app.UseHsts();
        }

        app.UseHttpsRedirection();
        app.UseStaticFiles();

        app.UseRouting();

        app.UseAuthorization();

        app.MapRazorPages();

        app.Run();
    }

  
}


