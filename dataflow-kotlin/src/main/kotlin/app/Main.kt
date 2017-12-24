package app

import org.apache.beam.sdk.Pipeline
import org.apache.beam.sdk.io.TextIO
import org.apache.beam.sdk.options.*
import org.apache.beam.sdk.transforms.*
import org.apache.beam.sdk.values.TypeDescriptors

interface MainOptions : PipelineOptions {
    @Description("input file")
    @Validation.Required
    @Default.String("gs://apache-beam-samples/shakespeare/*")
    fun getInputFile(): String

    fun setInputFile(value: String)

    @Description("output prefix")
    @Validation.Required
    fun getOutput(): String

    fun setOutput(value: String)
}

fun main(args: Array<String>) {
    val options = PipelineOptionsFactory.fromArgs(*args).withValidation().`as`(MainOptions::class.java)
    val p = Pipeline.create(options)

    p
        .apply("read text files", TextIO.read().from(options.getInputFile()))
        .apply(FlatMapElements.into(TypeDescriptors.strings()).via { line -> line.split("[^\\p{L}]+") })
        .apply("filter by word length", Filter.by(SerializableFunction { word: String -> !word.isEmpty() }))
        .apply("count words", Count.perElement<String>())
        .apply(MapElements.into(TypeDescriptors.strings()).via { wordCount -> wordCount.key + ": " + wordCount.value })
        .apply("write to file", TextIO.write().to(options.getOutput()))

    p.run().waitUntilFinish()
}