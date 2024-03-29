﻿using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using System.IO;
using System.Threading.Tasks;
using CsvHelper;
using Newtonsoft.Json;
using System.Globalization;
using System.Diagnostics;
using Newtonsoft.Json.Linq;
using static System.Runtime.InteropServices.JavaScript.JSType;
using System.Reflection;
using WessleyMitchell.Web.DotNetCore.ViewRenderer;

namespace test.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;

        [BindProperty]
        public IFormFile? Upload { get; set; }

        public IndexModel(ILogger<IndexModel> logger)
        {
            _logger = logger;
        }

        public void OnGet()
        {
        }

        [BindProperty]
        public string Description { get; set; }

        [BindProperty]
        public string Task { get; set; }



        public async Task<IActionResult> OnPostUploadFileAsync()
        {

            if (Upload != null && Upload.Length > 0)
            {
                var filePath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "uploads", Upload.FileName);

                using (var stream = new FileStream(filePath, FileMode.Create))
                {
                    await Upload.CopyToAsync(stream);
                    //TempData["Message"] = "<div class=\"alert fade_success .fade\"><strong>Success:</strong> File, description, and task Uploaded!</div>";

                }


                // Convert CSV to JSON
                var csvFilePath = filePath;  // Assuming Uploaded file is a CSV
                var jsonFilePath = Path.ChangeExtension(filePath, ".json");  // Change extension to .json

                using (var reader = new StreamReader(csvFilePath))
                using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
                {
                    var records = csv.GetRecords<dynamic>().ToList();

                    // Serialize to JSON
                    var json = JsonConvert.SerializeObject(records, Formatting.Indented);

                    // Write JSON to file
                    System.IO.File.WriteAllText(jsonFilePath, json);
                }

                //data extraction
                string jsonFileContent = System.IO.File.ReadAllText(jsonFilePath);
                JArray jsonArray = JArray.Parse(jsonFileContent);


                if (jsonArray.Count > 0)
                {
                    //tabela
                    string firstObjectString = jsonArray[0].ToString();
                    string secondObjectString = jsonArray[1].ToString();
                    //string triObjectString = jsonArray[1].ToString();
                    //string cetObjectString = jsonArray[1].ToString();
                    //string petObjectString = jsonArray[1].ToString();

                    string jsonString = $"[\n{firstObjectString},\n{secondObjectString}\n]";
                    string inputs = $"EXAMPLE OF DATA FROM JSON FILE:'{jsonString}', DESCRIPTION:'{Description}', FILE PATH:'{jsonFilePath}'";//task mora bit locen zarad py strukture
                    //dodaj collor picker

                    //prikaz tabele
                    TempData["JsonData"] = jsonString;

                    //run script
                    string pythonScriptPath = "/Users/timzav/Desktop/DataWizard/print.py";


                    // Create process start info
                    ProcessStartInfo psi = new()
                    {
                        FileName = "/Users/timzav/miniconda3/bin/python",
                        Arguments = $"{pythonScriptPath} {inputs} {Task}",
                        RedirectStandardOutput = true,
                        RedirectStandardError = true,
                        UseShellExecute = false,
                        CreateNoWindow = true
                    };

                    // Start the process
                    using Process process = new()
                    { StartInfo = psi };
                    process.Start();

                    string error;
                    //reading output and error streams
                    string output = process.StandardOutput.ReadToEnd();
                    error = process.StandardError.ReadToEnd();
                    process.WaitForExit();//wait for the process to finish
                    /*if (string.IsNullOrEmpty(error))
                    {
                        error = "none (running proccess {generate py})";
                    }*/
                    //nepotrebno

                    TempData["Message2"] = $"<div class=\"alert fade_success .fade\"><strong>Success:</strong> {output}</div>";
                    TempData["Message72"] = $"<div class=\"alert fade_error .fade\"><strong>ERROR:</strong> {error}</div>";

                }
                else
                {
                    Console.WriteLine("The JSON array is empty.");//zakaj je to tu
                }


                // END run script
            }
            else
            {
                TempData["Message"] = "<div class=\"alert fade_error .fade\"><strong>ERROR:</strong> File, description, or task not uploaded!</div>";
            }

            // Redirect back to the index page after the file is uploaded
            return RedirectToPage("/Index");

        }

        [HttpPost]
        public IActionResult OnPostTest(string ime)
        {
            string ime2 = "hello";
            return new JsonResult(ime2);
        }


        [HttpPost]
        public async Task<IActionResult> OnPostUploadAsync([FromBody] IFormFile? Upload)
        {
            var filePath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "uploads", Upload.FileName);

            using (var stream = new FileStream(filePath, FileMode.Create))
            {
                await Upload.CopyToAsync(stream);
               
            }


            // Convert CSV to JSON
            var csvFilePath = filePath;  // Assuming Uploaded file is a CSV
            var jsonFilePath = Path.ChangeExtension(filePath, ".json");  // Change extension to .json

            using (var reader = new StreamReader(csvFilePath))
            using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
            {
                var records = csv.GetRecords<dynamic>().ToList();

                // Serialize to JSON
                var json = JsonConvert.SerializeObject(records, Formatting.Indented);

                // Write JSON to file
                System.IO.File.WriteAllText(jsonFilePath, json);
            }

            //data extraction
            string jsonFileContent = System.IO.File.ReadAllText(jsonFilePath);
            JArray jsonArray = JArray.Parse(jsonFileContent);


            if (jsonArray.Count > 0)
            {
                //tabela
                string firstObjectString = jsonArray[0].ToString();
                string secondObjectString = jsonArray[1].ToString();
                //string triObjectString = jsonArray[1].ToString();
                //string cetObjectString = jsonArray[1].ToString();
                //string petObjectString = jsonArray[1].ToString();

                string jsonString = $"[\n{firstObjectString},\n{secondObjectString}\n]";
                string inputs = $"EXAMPLE OF DATA FROM JSON FILE:'{jsonString}', DESCRIPTION:'{Description}', FILE PATH:'{jsonFilePath}'";//task mora bit locen zarad py strukture
                                                                                                                                          //dodaj collor picker
                return new JsonResult(jsonString); }
             else
                {
                    string x  = ("The JSON array is empty.");//zakaj je to tu
                    return new JsonResult(x);
                }
           
        }
























    }

}
